# forms.py

from django import forms
from .models import Grado


class CursoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = '__all__'
