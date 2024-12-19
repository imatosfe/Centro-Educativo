from django.db import models

from grado.models import Grado

# Create your models here.
class Secciones(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name='secciones')
    fecha_termino = models.DateField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.grado.nombre}"