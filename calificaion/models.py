from django.db import models

from asignatura.models import Asignatura
from estudiante.models import Estudiante

# Create your models here.
class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificaciones')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='calificaciones')
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'asignatura')

    def __str__(self):
        return f"{self.estudiante} - {self.asignatura} - {self.nota}"