from django import forms
from django.utils import timezone
from .models import Estudiante
from bootstrap_datepicker_plus.widgets import DatePickerInput
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre', 
            'apellido', 
            'fecha_nacimiento', 
            'genero', 
            'email', 
            'telefono', 
            'direccion', 
            'ciudad', 
            'estado', 
   
            'matricula', 
            'fecha_ingreso', 
            
      
            'seccion', 
            'anio_escolar', 
      
        ]
        labels = {
            'nombre': 'Nombres',
            'apellido': 'Apellidos',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'genero': 'Género',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
      
            'estado': 'Estado',

            'ciudad': 'Provincias',
   
                'matricula': 'Matrícula',
                'fecha_ingreso': 'Fecha de Ingreso',
         
         
                'seccion': 'Sección',
                'anio_escolar': 'Año Escolar',
         


        }
        widgets = {
            'fecha_ingreso': DatePickerInput(format='%d-%m-%Y', attrs={'class': 'datepicker'}),
            'fecha_nacimiento': DatePickerInput(format='%d-%m-%Y', attrs={'class': 'datepicker'}),
        }
        placeholders  = {
            'nombre': 'Ingrese su nombre',
            'apellido': 'Ingrese su apellido',
            'email': 'Ingrese su correo electrónico',
            'telefono': 'Ingrese su teléfono',
            'direccion': 'Ingrese su dirección',
            'matricula': 'Ingrese su matrícula',
            'promedio': 'Ingrese su promedio',
            
            'seccion': 'Ingrese su sección',
            'anio_escolar': 'Ingrese su año escolar',
           
         }

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super(EstudianteForm, self).__init__(*args, **kwargs)
        # Agregar la clase 'datepicker' a los campos de fecha
        self.fields['fecha_nacimiento'].widget.attrs.update({'class': 'datepicker'})
        self.fields['fecha_ingreso'].widget.attrs.update({'class': 'datepicker'})

    # Agregar placeholders a los campos
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingrese su nombre'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Ingrese su apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese su correo electrónico'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Ingrese su teléfono'
        self.fields['direccion'].widget.attrs['placeholder'] = 'Ingrese su dirección'
        self.fields['matricula'].widget.attrs['placeholder'] = 'Ingrese su matrícula'
       
        self.fields['seccion'].widget.attrs['placeholder'] = 'Ingrese su sección'
        self.fields['anio_escolar'].widget.attrs['placeholder'] = 'Ingrese su año escolar'

      
  


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Estudiante.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento > timezone.now().date():
            raise forms.ValidationError("La fecha de nacimiento no puede ser una fecha futura.")
        return fecha_nacimiento

  