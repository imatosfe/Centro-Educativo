from datetime import timedelta
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from django.db import models
from django.utils import timezone
from .models import Estudiante, Factura, DetalleFactura, ConceptoFactura, PagoAdelantado
from .forms import PagoForm
from celery import shared_task



from django.http import HttpResponse

from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone


@shared_task
def generar_facturas_mensuales():
    hoy = timezone.now().date()
    primer_dia_mes = hoy.replace(day=1)
    ultimo_dia_mes = hoy.replace(day=1) + timedelta(days=31)

    estudiantes_activos = Estudiante.objects.filter(activo=True)

    for estudiante in estudiantes_activos:
        pago_adelantado = PagoAdelantado.objects.filter(estudiante=estudiante).first()

        # Si el estudiante pagó el 100% adelantado, no se generarán más facturas mensuales
        if pago_adelantado and pago_adelantado.tipo_pago == '100%':
            continue  # No generamos facturas si ya pagó el 100%

        for mes in range(9):  # Generar facturas solo para los 9 meses restantes del ciclo
            factura, creada = Factura.objects.get_or_create(
                estudiante=estudiante,
                fecha_emision=primer_dia_mes,
                fecha_vencimiento=ultimo_dia_mes,
                anio_escolar=hoy.year,
                mes=Factura.MESES_ESCOLAR[mes][0],  # Genera factura para cada mes
            )

            if creada:
                if pago_adelantado and pago_adelantado.tipo_pago == '50%':
                    # Si el estudiante pagó el 50%, solo facturar el 50% restante
                    monto_restante = estudiante.obtener_precio_anual() * 0.5 / 9  # 9 meses restantes
                    factura.monto_total = monto_restante
                else:
                    # Facturación normal (divide el total entre 10 meses)
                    factura.monto_total = estudiante.obtener_precio_anual() / 10

                factura.save()

                # Agregar el concepto de mensualidad
                concepto_mensualidad = ConceptoFactura.objects.get(nombre='Mensualidad')
                DetalleFactura.objects.create(
                    factura=factura,
                    concepto=concepto_mensualidad,
                    cantidad=1,
                    precio_unitario=factura.monto_total,
                )

def generar_facturas_view(request):
    # Aquí asumo que el estudiante está identificado de alguna manera
    estudiante_id = request.GET.get('estudiante_id')  # Obtén el ID del estudiante desde la solicitud
    estudiante = Estudiante.objects.get(id=estudiante_id)

    # Verificamos si el estudiante ya pagó el 100% del año escolar
    if not estudiante.has_pago_adelantado():  # Esto debe ser un método en el modelo Estudiante
        generar_facturas_mensuales.delay(estudiante_id)  # Llama a la tarea Celery para generar las facturas
        return HttpResponse("Las facturas se están generando.")
    else:
        return HttpResponse("Este estudiante ya ha pagado el 100% del año escolar, no se generarán facturas mensuales.")


def lista_facturas_pendientes(request):
    facturas_pendientes = Factura.objects.filter(estado='pendiente')
    return render(request, 'lista_facturas_pendientes.html', {'facturas': facturas_pendientes})

def procesar_pago(request, factura_id):
    factura = Factura.objects.get(pk=factura_id)

    if factura.pagada_completamente:
            messages.error(request, "La factura ya está pagada completamente.")
            return redirect('detalle_factura', factura_id=factura.id)
    

    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.factura = factura
            pago.save()
            factura.monto_pagado += pago.monto_pagado  # Asegurarse de que se añada el monto correcto
            factura.actualizar_estado()  # Asegúrate de que el estado se actualice
            factura.save()
            messages.success(request, "Pago registrado exitosamente.")
            return redirect('detalle_factura', factura_id=factura.id)
    else:
        form = PagoForm()
    return render(request, 'detalle_factura.html', {'factura': factura, 'form': form})


def detalle_factura(request, factura_id):
    factura = Factura.objects.get(pk=factura_id)
    
    if factura.pagada_completamente:
        messages.error(request, "La factura ya está pagada completamente.")
        return redirect('facturas_estudiante', estudiante_id=factura.estudiante.id)
    
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.factura = factura
            pago.save()
            factura.monto_pagado += pago.monto_pagado
            factura.actualizar_estado()  # Esto actualizará el estado de la factura

            # Agregar mensaje de confirmación
            messages.success(request, "Pago registrado exitosamente.")
            return redirect('detalle_factura', factura_id=factura.id)
    else:
        form = PagoForm()

    return render(request, 'detalle_factura.html', {'factura': factura, 'form': form})


from django.db import transaction

@transaction.atomic
def procesar_pago_adelantado(request, estudiante, tipo_pago):
    estudiante = get_object_or_404(Estudiante, id=estudiante)
    try:
        # Obtener el concepto de pago adelantado (50% o 100%)
        concepto_pago = ConceptoFactura.objects.get(nombre=tipo_pago, es_pago_adelantado=True)

        # Verificamos si el estudiante ya tiene un pago adelantado
        if estudiante.has_pago_adelantado():
            messages.warning(request, "Este estudiante ya tiene un pago adelantado registrado.")
            return redirect('detalle_estudiante', estudiante_id=estudiante.id)

        # Calcular el monto a pagar basado en el tipo de pago (50% o 100%)
        monto_a_pagar = concepto_pago.precio

        # Crear una factura de pago adelantado
        factura_adelantada = Factura.objects.create(
            estudiante=estudiante,
            anio_escolar=timezone.now().year,
            mes='Pago Adelantado',
            monto_total=monto_a_pagar,
            monto_pagado=monto_a_pagar,
            pagada_completamente=True,
            estado='Pagada'
        )

        # Agregar un detalle de pago adelantado a la factura
        DetalleFactura.objects.create(
            factura=factura_adelantada,
            concepto=concepto_pago,
            cantidad=1,
            precio_unitario=concepto_pago.precio,
        )

        # Si es 100% del año escolar, no se generan más facturas
        if tipo_pago == '100%':
            messages.success(request, f"Pago adelantado del 100% procesado correctamente para {estudiante.nombre}.")
            return redirect('detalle_factura', factura_id=factura_adelantada.id)

        # Si es 50%, aplicar el monto a las facturas pendientes
        facturas_pendientes = Factura.objects.filter(
            estudiante=estudiante, 
            pagada_completamente=False
        ).order_by('fecha_vencimiento')

        for factura in facturas_pendientes:
            if monto_a_pagar >= factura.monto_total - factura.monto_pagado:
                monto_a_pagar -= (factura.monto_total - factura.monto_pagado)
                factura.monto_pagado = factura.monto_total
                factura.pagada_completamente = True
                factura.estado = 'Pagada'
                factura.save()
            else:
                factura.monto_pagado += monto_a_pagar
                factura.estado = 'Pagada Parcialmente'
                factura.save()
                break

        # Verificamos si aún queda monto por pagar
        if monto_a_pagar <= 0:
            messages.success(request, f"Pago adelantado procesado correctamente para {estudiante.nombre}.")
        else:
            messages.warning(request, f"El pago adelantado no cubrió todas las facturas de {estudiante.nombre}. Queda un saldo pendiente.")

        return redirect('detalle_factura', factura_id=factura_adelantada.id)

    except ConceptoFactura.DoesNotExist:
        messages.error(request, "El concepto de pago adelantado no se encuentra registrado.")
    except Exception as e:
        messages.error(request, f"Hubo un error procesando el pago adelantado: {str(e)}")

    return redirect('detalle_estudiante', estudiante_id=estudiante.id)
