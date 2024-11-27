 
from django import views
from django.urls import path, re_path, reverse_lazy
from django.contrib.auth.decorators import login_required
from .views import (EditarPerfilView, RegistrarUsuario, Login)
from .views import cambiar_password
from . import views


urlpatterns = [
   # path('Registrar', RegistrarUsuario.as_view(), name='registro'),
     path('editar_usuario/<int:user_id>/', EditarPerfilView.as_view(), name='editar_usuario'),  # Ruta para editar un usuario existente

    path('cambiar-password/', cambiar_password, name='cambiar_password'),

    path('crear_usuario/', RegistrarUsuario.as_view(), name='crear_usuario'),  # Ruta para crear un nuevo usuario
  
  
 ]