from django.db import models
from estudiante.models import Estudiante
from django.core.validators import MinValueValidator



class ConceptoFactura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

class Factura(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='facturas')
    fecha_emision = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    anio_escolar = models.CharField(max_length=10)
    MESES = (
        ('Enero', 'Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre'),
    )
    mes = models.CharField(max_length=20, choices=MESES, default='Enero')  # Establecemos un valor por defecto
   
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagada_completamente = models.BooleanField(default=False)

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='detalles')
    concepto = models.ForeignKey(ConceptoFactura, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    metodo_pago = models.CharField(max_length=50)