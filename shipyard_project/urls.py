"""
URL configuration for shipyard_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views as home_views  # Import views from the 'home' app
from services import views as services_views  # Import views from the 'services' app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Home and About URLs
    path('', home_views.homepage, name='home'),  # Homepage URL
    path('about/', home_views.about, name='about'),

    # Admin Panel URLs
    path('admin-panel/', include('admin_panel.urls')),

    # Services URLs
    path('services/', home_views.services_view, name='services'),  # Services page URL
    path('services/ship-building/', services_views.ship_building, name='ship_building'),
    path('services/ship-repair/', services_views.ship_repair, name='ship_repair'),
    path('services/marine-engineering/', services_views.marine_engineering, name='marine_engineering'),
    path('services/financials/', services_views.financials, name='financials'),
    path('services/facilities/', services_views.facilities, name='facilities'),
    path('services/ship-building/thanks/', services_views.ship_building_thanks, name='ship_building_thanks'),

    # Tender URLs
    path('tender/', include('tender.urls')),

    # Vigilance URLs
    path('vigilance/', include('vigilance.urls')),

    # Teams URLs
    path('teams/', include('teams.urls')),

    # Stock Export URLs
    path('stock-export/', include('stock_export.urls')),  # Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)