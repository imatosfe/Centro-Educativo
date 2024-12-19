# urls.py
from django.urls import path
from .views import listar_notificaciones


urlpatterns = [
    path('', listar_notificaciones, name='listar_notificaciones'),
    
   
]
