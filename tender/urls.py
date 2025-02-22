from django.urls import path
from . import views

urlpatterns = [
    path('tender/', views.tender_list, name='tender_list'),  # Add trailing slash
    path('<int:pk>/', views.tender_detail, name='tender_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
]