from django.urls import path
from . import views

urlpatterns = [
    path('guidelines/', views.vigilance_guidelines, name='vigilance_guidelines'),
    path('report-issue/', views.report_issue, name='report_issue'),
    path('faq/', views.vigilance_faq, name='vigilance_faq'),
    path('thanks/', views.vigilance_thanks, name='vigilance_thanks'),
]