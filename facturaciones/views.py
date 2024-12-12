from datetime import timedelta
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.db import models
from django.utils import timezone
from .models import Estudiante, Factura, DetalleFactura, ConceptoFactura
from .forms import PagoForm
from celery import shared_task

@shared_task
def generar_facturas_mensuales():
    hoy = timezone.now().date()
    primer_dia_mes = hoy.replace(day=1)
    ultimo_dia_mes = hoy.replace(day=1) + timedelta(days=31)

    estudiantes_activos = Estudiante.objects.filter(activo=True)
    concepto_mensualidad = ConceptoFactura.objects.get(nombre='Mensualidad')

    for estudiante in estudiantes_activos:
        factura, creada = Factura.objects.get_or_create(
            estudiante=estudiante,
            fecha_emision=primer_dia_mes,
            fecha_vencimiento=ultimo_dia_mes,
            defaults={
                'anio_escolar': hoy.year,
                'mes': hoy.strftime('%B'),  # Nombre del mes en español
            }
        )

        if creada:
            DetalleFactura.objects.create(
                factura=factura,
                concepto=concepto_mensualidad,
                cantidad=1,  # Ajusta la cantidad según sea necesario
                precio_unitario=concepto_mensualidad.precio,
            )

def lista_facturas_pendientes(request):
    facturas_pendientes = Factura.objects.filter(estado='pendiente')
    return render(request, 'lista_facturas_pendientes.html', {'facturas': facturas_pendientes})

def detalle_factura(request, factura_id):
    factura = Factura.objects.get(pk=factura_id)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.factura = factura
            pago.save()
            # Actualizar el monto pagado y estado de la factura
            factura.monto_pagado += pago.monto
            factura.save()
            # Agregar mensaje de confirmación
            messages.success(request, "Pago registrado exitosamente.")
            return redirect('detalle_factura', factura_id=factura.id)
    else:
        form = PagoForm()
    return render(request, 'detalle_factura.html', {'factura': factura, 'form': form})