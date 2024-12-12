from django.urls import path
from . import views

urlpatterns = [
    path('lista-facturas-pendientes/', views.lista_facturas_pendientes, name='lista_facturas_pendientes'),
    path('detalle-factura/<int:factura_id>/', views.detalle_factura, name='detalle_factura'),
]