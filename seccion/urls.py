from django.urls import path
from .views import (
    # Importación de vistas ya creadas
    SeccionListView, SeccionDetailView, SeccionCreateView, SeccionUpdateView, SeccionDeleteView,
    ProfesorListView, ProfesorDetailView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,
    AsignaturaListView, AsignaturaDetailView, AsignaturaCreateView, AsignaturaUpdateView, AsignaturaDeleteView,
)

urlpatterns = [
    # Secciones
    path('secciones/', SeccionListView.as_view(), name='seccion-list'),
    path('secciones/<int:pk>/', SeccionDetailView.as_view(), name='seccion-detail'),
    path('secciones/create/', SeccionCreateView.as_view(), name='seccion-create'),
    path('secciones/<int:pk>/update/', SeccionUpdateView.as_view(), name='seccion-update'),
    path('secciones/<int:pk>/delete/', SeccionDeleteView.as_view(), name='seccion-delete'),

]
