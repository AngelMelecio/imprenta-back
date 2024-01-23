from django.urls import path
from apps.Prensa.api import prensa_api_view,prensa_detail_api_view

urlpatterns = [
    path('prensas/', prensa_api_view, name='prensas_api'),
    path('prensas/<int:pk>', prensa_detail_api_view, name='prensa_detail_api_view'),
]