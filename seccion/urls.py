# secciones/urls.py
from django.urls import path
from . import views
from .views import crear_seccion, eliminar_seccion, editar_seccion, lista_secciones

urlpatterns = [
    path('', lista_secciones, name='lista_secciones'),
    path('crear-seccion/', crear_seccion, name='crear_seccion'),
   path('editar-seccion/<int:seccion_id>/', editar_seccion, name='editar_seccion'),
      
    path('eliminar-seccion/<int:seccion_id>/',eliminar_seccion, name='eliminar_seccion'),

]   

