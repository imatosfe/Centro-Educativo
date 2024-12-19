# forms.py
from django import forms
from .models import Calificacion
from estudiante.models import Estudiante
from asignatura.models import Asignatura


from django import forms

class CalificacionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        seccion = kwargs.pop('seccion')  # Recibe la sección desde la vista
        super().__init__(*args, **kwargs)

        # Añadir dinámicamente los campos de calificación para cada asignatura
        asignaturas = Asignatura.objects.filter(grado=seccion.grado)
        for asignatura in asignaturas:
            self.fields[f'nota_{asignatura.id}'] = forms.DecimalField(
                required=False,
                label=f'Calificación de {asignatura.nombre}',
                widget=forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'})
            )
