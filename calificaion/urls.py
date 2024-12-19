from django.urls import path
from .views import (
  CalificacionListView, CalificacionCreateView, ReporteCalificacionesPorEstudianteView
)
from . import views
urlpatterns = [
    path('calificaciones/secciones/', views.listar_secciones, name='listar_secciones'),
    path('calificaciones/seccion/<int:seccion_id>/estudiantes/', views.listar_estudiantes_calificacion, name='listar_estudiantes_calificacion'),
    path('calificaciones/seccion/<int:seccion_id>/estudiantes/<int:estudiante_id>/calificaciones/agregar/', views.agregar_calificacion, name='agregar_calificacion'),
      path('calificaciones/estudiante/<int:estudiante_id>/por_grado/', views.calificaciones_por_grado, name='calificaciones_por_grado'),

    # Calificaciones
    path('calificaciones/', CalificacionListView.as_view(), name='calificacion-list'),
    path('calificaciones/create/', CalificacionCreateView.as_view(), name='calificacion-create'),
    path('reportes/estudiante/<int:estudiante_id>/', ReporteCalificacionesPorEstudianteView.as_view(), name='reporte-estudiante'),
]
