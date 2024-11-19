from django.urls import path
from .views import (
    AulaListView, AulaDetailView, AulaCreateView, AulaUpdateView, AulaDeleteView,
    GradoListView, GradoDetailView, GradoCreateView, GradoUpdateView, GradoDeleteView,
    EstudianteListView, EstudianteDetailView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView,
    CalificacionListView, CalificacionCreateView, ReporteCalificacionesPorEstudianteView
)

urlpatterns = [

    # Grados
    path('grados/', GradoListView.as_view(), name='grado-list'),
    path('grados/<int:pk>/', GradoDetailView.as_view(), name='grado-detail'),
    path('grados/create/', GradoCreateView.as_view(), name='grado-create'),
    path('grados/<int:pk>/update/', GradoUpdateView.as_view(), name='grado-update'),
    path('grados/<int:pk>/delete/', GradoDeleteView.as_view(), name='grado-delete'),
]
