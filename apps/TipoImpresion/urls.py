from django.urls import path
from apps.TipoImpresion.api import tipoImpresion_api_view,tipoImpresion_detail_api_view

urlpatterns = [
    path('tipoImpresiones/', tipoImpresion_api_view, name='tipoImpresiones_api'),
    path('tipoImpresiones/<int:pk>', tipoImpresion_detail_api_view, name='tipoImpresion_detail_api_view'),
]