
from django.urls import path

from asignatura import views

urlpatterns = [
    
    # Asignaturas
 #  path('', AsignaturaListView.as_view(), name='asignatura-list'),
 #   path('asignaturas/<int:pk>/', AsignaturaDetailView.as_view(), name='asignatura-detail'),
  #  path('asignaturas/create/', AsignaturaCreateView.as_view(), name='asignatura-create'),
 #   path('asignaturas/<int:pk>/update/', AsignaturaUpdateView.as_view(), name='asignatura-update'),
  #  path('asignaturas/<int:pk>/delete/', AsignaturaDeleteView.as_view(), name='asignatura-delete'),

       
       path('', views.lista_asignatura, name='asignatura-list'),
       path('asignatura/eliminar/<int:asignatura_id>/', views.eliminar_asignatura, name='eliminar_asignatura'),
       path('crear', views.crear_asignatura, name='crear_asignatura'),

 path('asignatura/editar/<int:asignatura_id>/', views.actualizar_asignatura, name='actualizar_asignatura'),
]
