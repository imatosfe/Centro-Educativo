from django import forms
from .models import Factura, Pago, ConceptoFactura, Estudiante

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['estudiante', 'fecha_vencimiento', 'anio_escolar', 'mes']
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'anio_escolar': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['mes'].empty_label = "Seleccionar mes"  

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['monto_pagado', 'metodo_pago']
        widgets = {
            'monto_pagado': forms.NumberInput(attrs={'class': 'form-control'}),
            'metodo_pago': forms.TextInput(attrs={'class': 'form-control'}),
        }