from django.contrib import admin
from .models import Grievance, FAQ

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'complaint_type', 'submitted_at')
    search_fields = ('name', 'complaint_type')
    list_filter = ('complaint_type', 'submitted_at')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)