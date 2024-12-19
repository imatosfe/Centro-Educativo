from celery import shared_task
from .models import Notificacion, Secciones
from datetime import timedelta
from django.utils.timezone import now
from django.shortcuts import render
import logging
from django.shortcuts import get_object_or_404, redirect
# Configurar logger para la tarea Celery
logger = logging.getLogger(__name__)

from django.shortcuts import render
from notificaciones.tasks import generar_notificaciones_secciones

# Configurar el logger para la tarea
logger = logging.getLogger(__name__)

@shared_task
def generar_notificaciones_secciones():
    hoy = now().date()
    proximos_dias = hoy + timedelta(days=7)
    notificaciones = []

    # Optimización de la consulta
    secciones = Secciones.objects.filter(fecha_termino__range=(hoy, proximos_dias)).select_related('grado')

    logger.info(f"Secciones encontradas: {secciones.count()}")

    for seccion in secciones:
        titulo = f"Sección {seccion.nombre} próxima a finalizar"
        mensaje = f"La sección {seccion.nombre} del curso {seccion.grado.nombre} finalizará el {seccion.fecha_termino}."

        try:
            notificacion, created = Notificacion.objects.get_or_create(
                titulo=titulo,
                mensaje=mensaje,
                seccion=seccion
            )
            logger.info(f"Notificación {'creada' if created else 'ya existente'}: {notificacion.titulo}")
            notificaciones.append(notificacion)
        except Exception as e:
            logger.error(f"Error al crear notificación para la sección {seccion.nombre}: {e}")

    return f"{len(notificaciones)} notificaciones generadas."


def generar_notificaciones(request):
    # Llamar a la tarea de Celery para que se ejecute en segundo plano
    generar_notificaciones_secciones.delay()
    return render(request, 'notificaciones/exito.html')

# Vista para listar las notificaciones
def listar_notificaciones(request):
    generar_notificaciones_secciones()
    # Obtener todas las notificaciones y ordenarlas por fecha de creación
    notificaciones = Notificacion.objects.all().order_by('-fecha_creacion')

    # Usar paginator para mejorar el rendimiento si hay muchas notificaciones
    from django.core.paginator import Paginator
    paginator = Paginator(notificaciones, 10)  # Muestra 10 notificaciones por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Mostrar el contenido de las notificaciones en el log para depuración (opcional)
    logger.info(f"Mostrando página {page_obj.number} de notificaciones")

    # Renderizar la plantilla con las notificaciones
    context = {'notificaciones': page_obj}
    return render(request, 'notificaciones/listar.html', context)

