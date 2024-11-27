from django.urls import path
from .views import crear_estudiante, lista_estudiantes, eliminar_estudiante, editar_estudiante
from django.conf import settings


from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('crear/', crear_estudiante, name='crear_estudiante'),
    path('', lista_estudiantes, name='lista_estudiantes'),  # Página principal con la lista de estudiantes

        path('editar/<int:estudiante_id>/', editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:estudiante_id>/', eliminar_estudiante, name='eliminar_estudiante'),

    # Agrega aquí las rutas para editar y eliminar estudiantes si es necesario
]
