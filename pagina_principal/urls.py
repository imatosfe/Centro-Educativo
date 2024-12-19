# principal/urls.py

from django.urls import path
from . import views
from .views import  marcar_como_leida

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL para la página principal
       path('dashboard', views.inicio2, name='inicio2'),  # URL para la página principal
           path('notificaciones/marcar-como-leida/<int:notificacion_id>/', marcar_como_leida, name='marcar_como_leida'),

]

