from django.urls import path
from .views import (
    AulaListView, AulaDetailView, AulaCreateView, AulaUpdateView, AulaDeleteView,
    GradoListView, GradoDetailView, GradoCreateView, GradoUpdateView, GradoDeleteView,
    EstudianteListView, EstudianteDetailView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView,
    CalificacionListView, CalificacionCreateView, ReporteCalificacionesPorEstudianteView
)

urlpatterns = [

    # Estudiantes
    path('estudiantes/', EstudianteListView.as_view(), name='estudiante-list'),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name='estudiante-detail'),
    path('estudiantes/create/', EstudianteCreateView.as_view(), name='estudiante-create'),
    path('estudiantes/<int:pk>/update/', EstudianteUpdateView.as_view(), name='estudiante-update'),
    path('estudiantes/<int:pk>/delete/', EstudianteDeleteView.as_view(), name='estudiante-delete'),
]
