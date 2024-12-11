# forms.py
from django import forms
from .models import Calificacion
from estudiante.models import Estudiante
from asignatura.models import Asignatura

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'asignatura', 'nota']

    # Añadimos un campo extra para asignar solo las asignaturas de la sección del estudiante
    def __init__(self, *args, **kwargs):
        seccion = kwargs.pop('seccion')  # Recibir la sección en la vista
        super().__init__(*args, **kwargs)
        self.fields['asignatura'].queryset = Asignatura.objects.filter(grado=seccion.grado)
