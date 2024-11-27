from django.urls import path
from .views import (
  
    ProfesorListView, ProfesorDetailView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView,

)

urlpatterns = [

    # Profesores
    path('profesores/', ProfesorListView.as_view(), name='profesor-list'),
    path('profesores/<int:pk>/', ProfesorDetailView.as_view(), name='profesor-detail'),
    path('profesores/create/', ProfesorCreateView.as_view(), name='profesor-create'),
    path('profesores/<int:pk>/update/', ProfesorUpdateView.as_view(), name='profesor-update'),
    path('profesores/<int:pk>/delete/', ProfesorDeleteView.as_view(), name='profesor-delete'),
]
