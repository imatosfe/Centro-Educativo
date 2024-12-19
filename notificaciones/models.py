from django.db import models

# Create your models here.
# notificaciones/models.py
from django.db import models
from estudiante.models import Estudiante
from seccion.models import Secciones
from django.utils.timezone import now

class Notificacion(models.Model):
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    seccion = models.ForeignKey(Secciones, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
