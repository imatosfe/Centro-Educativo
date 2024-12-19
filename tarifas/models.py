from django.db import models
from grado.models import Grado


class TarifaEscolar(models.Model):
    grado = models.OneToOneField(Grado, on_delete=models.CASCADE, related_name='tarifa_escolar')
    precio_anual = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_precio_mensual(self):
        return self.precio_anual / 12

    def __str__(self):
        return f"Tarifa {self.grado.nombre} - {self.precio_anual} DOP"
