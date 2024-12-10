# urls.py

from django.urls import path
from .views import (
    ProfesorListView,
    ProfesorCreateView,
    ProfesorUpdateView,

)
from .views import  eliminar_profesor

urlpatterns = [
    path('', ProfesorListView.as_view(), name='lista_profesores'),
    path('profesores/nuevo/', ProfesorCreateView.as_view(), name='crear_profesor'),
    path('profesores/<int:pk>/editar/', ProfesorUpdateView.as_view(), name='editar_profesor'),
    path('eliminar/<int:profesor_id>/',eliminar_profesor, name='eliminar_profesor'),
]
