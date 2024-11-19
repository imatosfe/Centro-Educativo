from django.db import models

from grado.models import Grado

# Create your models here.
class Seccion(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name='secciones')

    def __str__(self):
        return f"{self.nombre} - {self.grado.nombre}"