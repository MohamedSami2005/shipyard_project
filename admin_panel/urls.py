from django.urls import path
from . import views

urlpatterns = [
    path('ship-building/', views.ship_building_list, name='ship_building_list'),
    path('ship-building/update/<int:pk>/', views.ship_building_update, name='ship_building_update'),
    path('ship-building/delete/<int:pk>/', views.ship_building_delete, name='ship_building_delete'),

    path('ship-repair/', views.ship_repair_list, name='ship_repair_list'),
    path('ship-repair/update/<int:pk>/', views.ship_repair_update, name='ship_repair_update'),
    path('ship-repair/delete/<int:pk>/', views.ship_repair_delete, name='ship_repair_delete'),
    # Marine Engineering URLs
    path('marine-engineering/', views.marine_engineering_list, name='marine_engineering_list'),
    path('marine-engineering/create/', views.marine_engineering_create, name='marine_engineering_create'),
    path('marine-engineering/update/<int:pk>/', views.marine_engineering_update, name='marine_engineering_update'),
    path('marine-engineering/delete/<int:pk>/', views.marine_engineering_delete, name='marine_engineering_delete'),
]