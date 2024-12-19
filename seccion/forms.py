# secciones/forms.py
from django import forms
# from estudiantes.models import Estudiante
from .models import Secciones
from bootstrap_datepicker_plus.widgets import DatePickerInput

class SeccionForm(forms.ModelForm):
    

     class Meta:
        model = Secciones  # Asegúrate de que este es tu modelo
        fields = ['nombre', 'grado' , 'fecha_termino', 'fecha_inicio']  # Otros campos que necesites
        widgets = {
         
               'fecha_termino': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      
        }
 



