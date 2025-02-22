# inventory/views.py
from django.shortcuts import render
from .models import Inventory

def view_inventory(request):
    inventory = Inventory.objects.all()
    return render(request, 'inventory/view.html', {'inventory': inventory})