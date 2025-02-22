# stock_export/admin.py
from django.contrib import admin
from .models import StockExportRequest

class StockExportRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'stock_name', 'stock_category', 'destination_country', 'created_at')
    list_filter = ('stock_category', 'destination_country')
    search_fields = ('stock_name', 'company_name')
    readonly_fields = ('created_at',)  # Make created_at read-only

admin.site.register(StockExportRequest, StockExportRequestAdmin)