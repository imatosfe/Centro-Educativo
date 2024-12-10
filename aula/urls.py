from django.urls import path
from .views import (
    # Importación de vistas ya creadas
    AulaCreateView, AulaDeleteView, AulaDetailView, AulaListView, AulaUpdateView,  eliminar_aula
)

urlpatterns = [
    path('', AulaListView.as_view(), name='aula-list'),
    path('<int:pk>/', AulaDetailView.as_view(), name='aula-detail'),
    path('<int:pk>/editar/', AulaUpdateView.as_view(), name='aula-update'),
    path('crear/', AulaCreateView.as_view(), name='aula-create'),
    path('<int:pk>/eliminar/', AulaDeleteView.as_view(), name='aula-delete'),
    path('eliminar/<int:aula_id>/', eliminar_aula, name='eliminar-aula'),
]
