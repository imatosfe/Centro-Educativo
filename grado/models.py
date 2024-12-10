from django.db import models

from aula.models import Aula

# Create your models here.
class Grado(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='grados')

    def __str__(self):
        return self.nombre