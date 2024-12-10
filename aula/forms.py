from django import forms
from .models import Aula

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
