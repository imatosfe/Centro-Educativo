from django.urls import path
from .views import (
    # Importación de vistas ya creadas
    SeccionListView, SeccionDetailView, SeccionCreateView, SeccionUpdateView, SeccionDeleteView,
    ProfesorListView, ProfesorDetailView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,
    AsignaturaListView, AsignaturaDetailView, AsignaturaCreateView, AsignaturaUpdateView, AsignaturaDeleteView,
)

urlpatterns = [

    # Profesores
    path('profesores/', ProfesorListView.as_view(), name='profesor-list'),
    path('profesores/<int:pk>/', ProfesorDetailView.as_view(), name='profesor-detail'),
    path('profesores/create/', ProfesorCreateView.as_view(), name='profesor-create'),
    path('profesores/<int:pk>/update/', ProfesorUpdateView.as_view(), name='profesor-update'),
    path('profesores/<int:pk>/delete/', ProfesorDeleteView.as_view(), name='profesor-delete'),
]
