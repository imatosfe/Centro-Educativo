from django.urls import path
from .views import (
    # Importación de vistas ya creadas
    SeccionListView, SeccionDetailView, SeccionCreateView, SeccionUpdateView, SeccionDeleteView,
    ProfesorListView, ProfesorDetailView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,
    AsignaturaListView, AsignaturaDetailView, AsignaturaCreateView, AsignaturaUpdateView, AsignaturaDeleteView,
)

urlpatterns = [
    
    # Asignaturas
    path('asignaturas/', AsignaturaListView.as_view(), name='asignatura-list'),
    path('asignaturas/<int:pk>/', AsignaturaDetailView.as_view(), name='asignatura-detail'),
    path('asignaturas/create/', AsignaturaCreateView.as_view(), name='asignatura-create'),
    path('asignaturas/<int:pk>/update/', AsignaturaUpdateView.as_view(), name='asignatura-update'),
    path('asignaturas/<int:pk>/delete/', AsignaturaDeleteView.as_view(), name='asignatura-delete'),
]
