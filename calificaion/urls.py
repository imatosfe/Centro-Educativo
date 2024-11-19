from django.urls import path
from .views import (
    AulaListView, AulaDetailView, AulaCreateView, AulaUpdateView, AulaDeleteView,
    GradoListView, GradoDetailView, GradoCreateView, GradoUpdateView, GradoDeleteView,
    EstudianteListView, EstudianteDetailView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView,
    CalificacionListView, CalificacionCreateView, ReporteCalificacionesPorEstudianteView
)

urlpatterns = [

    # Calificaciones
    path('calificaciones/', CalificacionListView.as_view(), name='calificacion-list'),
    path('calificaciones/create/', CalificacionCreateView.as_view(), name='calificacion-create'),
    path('reportes/estudiante/<int:estudiante_id>/', ReporteCalificacionesPorEstudianteView.as_view(), name='reporte-estudiante'),
]
