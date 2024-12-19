from django.urls import path
from . import views

urlpatterns = [
    # URL para generar las facturas mensuales
    path('generar_facturas/', views.generar_facturas_view, name='generar_facturas'),

    # URL para mostrar las facturas pendientes
    path('facturas/pendientes/', views.lista_facturas_pendientes, name='lista_facturas_pendientes'),

    # URL para procesar un pago
    path('procesar_pago/<int:fatura_id>/', views.procesar_pago, name='procesar_pago'),

    # URL para ver los detalles de una factura
    path('detalle_factura/<int:fatura_id>/', views.detalle_factura, name='detalle_factura'),

    # URL para procesar un pago adelantado
    path('procesar_pago_adelantado/<int:estudiante_id>/<str:tipo_pago>/', views.procesar_pago_adelantado, name='procesar_pago_adelantado'),
    
    # URL para el detalle de un estudiante
]
