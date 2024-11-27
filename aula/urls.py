from django.urls import path
from .views import (
    # Importación de vistas ya creadas
    AulaCreateView, AulaDeleteView, AulaDetailView, AulaListView, AulaUpdateView
)

urlpatterns = [
    path('aulas/', AulaListView.as_view(), name='aula-list'),
    path('aulas/<int:pk>/', AulaDetailView.as_view(), name='aula-detail'),
    path('aulas/create/', AulaCreateView.as_view(), name='aula-create'),
    path('aulas/<int:pk>/update/', AulaUpdateView.as_view(), name='aula-update'),
    path('aulas/<int:pk>/delete/', AulaDeleteView.as_view(), name='aula-delete'),
]
