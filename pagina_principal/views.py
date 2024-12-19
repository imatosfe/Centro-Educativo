from datetime import timedelta
from celery import shared_task
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from notificaciones.views import generar_notificaciones_secciones
from seccion.models import Secciones

from django.utils.timezone import now

def inicio(request):
    try:
        return render(request, 'pagina_principal/templates/pagina_principal/landin.html', {})
    except Exception as e:
      
        # Return a default response if there is an error
        return render(request, 'pagina_principal/landin.html', {'error_message': str(e)})


import logging

# Create a logger
logger = logging.getLogger(__name__)
from django.shortcuts import render

from datetime import timedelta
from django.utils.timezone import now
import logging
from notificaciones.models import Notificacion

# Configurar logger
logger = logging.getLogger(__name__)







#@login_required
def inicio2(request):
    try:
        user = request.user  # Obteniendo el usuario autenticado
        logger.info(f'Usuario autenticado: {user.username}')
        conteo_notificaciones = Notificacion.objects.filter(leida=False).count()  # Contar notificaciones no leídas
   #     logger.info(f'Notificaciones no leídas: {conteo_notificaciones}')
    
        
        return render(request, 'inicio2.html', {
            'user': user,
             
   #         'conteo_notificaciones': conteo_notificaciones,
           
        })
    
    except Exception as e:
        logger.error(f'Error en la vista inicio: {str(e)}')
        return render(request, 'pagina_principal/inicio2.html', {'error_message': str(e)})


from django.shortcuts import redirect, get_object_or_404
from notificaciones.models import Notificacion

def marcar_como_leida(request, notificacion_id):
    # Obtener la notificación
    notificacion = get_object_or_404(Notificacion, id=notificacion_id)

    # Marcarla como leída
    notificacion.leido = True
    notificacion.save()

    # Redirigir al usuario a la página principal (o la página de notificaciones)
    return redirect('listar_notificaciones')  # Si tu URL de página principal se llama 'pagina_principal'






