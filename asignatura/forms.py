from django import forms
from .models import Asignatura

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'grado', 'profesor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.Select(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-control'}),
        }
