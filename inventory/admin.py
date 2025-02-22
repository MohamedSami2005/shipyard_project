# inventory/admin.py
from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('stock_name', 'stock_type', 'quantity', 'warehouse_location', 'availability_status')
    list_filter = ('stock_type', 'warehouse_location')
    search_fields = ('stock_name', 'warehouse_location')