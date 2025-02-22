from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_page, name='teams_page'),
]