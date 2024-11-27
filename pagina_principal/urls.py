# principal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # URL para la página principal
       path('dashboard', views.inicio2, name='inicio2'),  # URL para la página principal
]

