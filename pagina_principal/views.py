from django.shortcuts import render

# Create your views here.



def inicio(request):
    try:
        return render(request, 'pagina_principal/templates/pagina_principal/landin.html', {})
    except Exception as e:
      
        # Return a default response if there is an error
        return render(request, 'pagina_principal/templates/pagina_principal/landin.html', {'error_message': str(e)})


import logging

# Create a logger
logger = logging.getLogger(__name__)

#@login_required
def inicio2(request):
    try:
        user = request.user  # Obteniendo el usuario autenticado
        logger.info(f'Usuario autenticado: {user.username}')
     #   conteo_notificaciones = Notificacion.objects.filter(leida=False).count()  # Contar notificaciones no leídas
   #     logger.info(f'Notificaciones no leídas: {conteo_notificaciones}')
    #    notificaciones = Notificacion.objects.filter(leida=False)  # Obtener notificaciones no leídas
   #     logger.info(f'Notificaciones obtenidas: {notificaciones.count()}')
        return render(request, 'inicio2.html', {
            'user': user,
   #         'conteo_notificaciones': conteo_notificaciones,
  #          'notificaciones': notificaciones,
        })
    except Exception as e:
        logger.error(f'Error en la vista inicio: {str(e)}')
        return render(request, 'inicio2.html', {'error_message': str(e)})
