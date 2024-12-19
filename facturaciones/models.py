from django.db import models
from estudiante.models import Estudiante
from django.core.validators import MinValueValidator
from django.apps import apps

class PagoAdelantado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='pagos_adelantados')
    fecha_pago = models.DateField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    tipo_pago = models.CharField(
        max_length=20,
        choices=[('50%', '50% del año escolar'), ('100%', '100% del año escolar')],
        default='50%',
    )
    def calcular_monto_total(self):
        precio_anual = self.estudiante.obtener_precio_anual()  # Asumiendo que este método existe
        if self.tipo_pago == '50%':
            return precio_anual * 0.5
        elif self.tipo_pago == '100%':
            return precio_anual
        
    # En facturaciones/models.py
    def obtener_estudiantes(self):
        Estudiante = apps.get_model('estudiante', 'Estudiante')  # Cargar modelo de forma diferida
        estudiantes = Estudiante.objects.all()
        return estudiantes



class ConceptoFactura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    es_pago_adelantado = models.BooleanField(default=False)  # Para pagos adelantados (50% o 100%)
    es_inscripcion = models.BooleanField(default=False)  # Para el concepto de inscripción
    es_anio_escolar = models.BooleanField(default=False)  # Para el año escolar completo
    es_mensualidad = models.BooleanField(default=False)  # Para la mensualidad


class Factura(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='facturas')
    fecha_emision = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    anio_escolar = models.CharField(max_length=10)
    
    MESES_ESCOLAR = (
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
    )
    mes = models.CharField(max_length=20, choices=MESES_ESCOLAR)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagada_completamente = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=[
        ('Pendiente', 'Pendiente'),
        ('Pagada Parcialmente', 'Pagada Parcialmente'),
        ('Pagada', 'Pagada'),
    ], default='Pendiente')

    def actualizar_estado(self):
        if self.monto_pagado >= self.monto_total:
            self.pagada_completamente = True
            self.estado = 'Pagada'
        elif self.monto_pagado > 0:
            self.estado = 'Pagada Parcialmente'
        else:
            self.estado = 'Pendiente'
        self.save()

    def calcular_monto_total(self):
        if self.estudiante.has_pago_adelantado():  # Suponiendo que tienes un método que chequea si el estudiante pagó
            return 0  # No se facturará si ya pagó el total del año escolar
        else:
            precio_anual = self.estudiante.obtener_precio_anual()
            precio_mensual = precio_anual / 10  # Dividir el precio total del año entre 10 meses
            return precio_mensual


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    concepto = models.ForeignKey(ConceptoFactura, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)  # Se puede establecer 1 por defecto, ya que generalmente es 1 concepto
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Detalle de {self.factura} - {self.concepto.nombre}"

    @property
    def total_detalle(self):
        """Calcula el monto total de este detalle (cantidad * precio unitario)"""
        return self.cantidad * self.precio_unitario


class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    metodo_pago = models.CharField(
        max_length=50,
        choices=[
            ('Tarjeta de Crédito', 'Tarjeta de Crédito'),
            ('Transferencia Bancaria', 'Transferencia Bancaria'),
            ('Efectivo', 'Efectivo'),
            ('Cheque', 'Cheque'),
            ('Otro', 'Otro'),
        ],
        default='Otro'
    )

    def __str__(self):
        return f"Pago de {self.monto_pagado} - {self.metodo_pago} - {self.fecha_pago}"

    @property
    def es_pago_completo(self):
        """Determina si el pago cubre el total de la factura"""
        return self.monto_pagado >= self.factura.monto_total

