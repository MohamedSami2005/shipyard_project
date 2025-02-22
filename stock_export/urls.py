# stock_export/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.stock_export_request, name='stock_export_request'),
    path('success/', views.stock_export_success, name='stock_export_success'),
]