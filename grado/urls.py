
# cursos/urls.py
from django.urls import path
from . import views
from .views import  eliminar_curso

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),            # Listar todos los cursos
    path('crear/', views.crear_curso, name='crear_curso'),        # Crear un nuevo curso
    path('detalle/<int:pk>/', views.detalle_curso, name='detalle_curso'), # Ver detalles de un curso específico
path('editar/<int:curso_id>/update/', views.editar_curso, name='editar_curso'),


    path('eliminar/<int:pk>/delete/',eliminar_curso, name='eliminar_curso'),
]
