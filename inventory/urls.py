# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_inventory, name='view_inventory'),
]