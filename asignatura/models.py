from django.db import models

from grado.models import Grado
from profesor.models import Profesor

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name='asignaturas')
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True, related_name='asignaturas')
    fecha_termino = models.DateField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre