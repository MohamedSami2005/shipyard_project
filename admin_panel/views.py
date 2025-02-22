from django.shortcuts import render, get_object_or_404, redirect
from services.models import ShipBuildingOrder, ShipRepairComplaint, MarineEngineering
from services.forms import ShipBuildingOrderForm, ShipRepairComplaintForm, MarineEngineeringForm

# Ship Building Views
def ship_building_list(request):
    orders = ShipBuildingOrder.objects.all()  # Fetch all shipbuilding orders
    return render(request, 'admin_panel/ship_building_list.html', {'orders': orders})

def ship_building_update(request, pk):
    order = get_object_or_404(ShipBuildingOrder, pk=pk)
    if request.method == 'POST':
        form = ShipBuildingOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('ship_building_list')
    else:
        form = ShipBuildingOrderForm(instance=order)
    return render(request, 'admin_panel/ship_building_form.html', {'form': form})

def ship_building_delete(request, pk):
    order = get_object_or_404(ShipBuildingOrder, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('ship_building_list')
    return render(request, 'admin_panel/ship_building_confirm_delete.html', {'order': order})

# Ship Repair Views
def ship_repair_list(request):
    repairs = ShipRepairComplaint.objects.all()  # Fetch all ship repair complaints
    return render(request, 'admin_panel/ship_repair_list.html', {'repairs': repairs})

def ship_repair_update(request, pk):
    repair = get_object_or_404(ShipRepairComplaint, pk=pk)
    if request.method == 'POST':
        form = ShipRepairComplaintForm(request.POST, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('ship_repair_list')
    else:
        form = ShipRepairComplaintForm(instance=repair)
    return render(request, 'admin_panel/ship_repair_form.html', {'form': form})

def ship_repair_delete(request, pk):
    repair = get_object_or_404(ShipRepairComplaint, pk=pk)
    if request.method == 'POST':
        repair.delete()
        return redirect('ship_repair_list')
    return render(request, 'admin_panel/ship_repair_confirm_delete.html', {'repair': repair})


# Marine Engineering Views
def marine_engineering_list(request):
    marine_engineers = MarineEngineering.objects.all()
    return render(request, 'admin_panel/marine_engineering_list.html', {'marine_engineers': marine_engineers})

def marine_engineering_create(request):
    if request.method == 'POST':
        form = MarineEngineeringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('marine_engineering_list')
    else:
        form = MarineEngineeringForm()
    return render(request, 'admin_panel/marine_engineering_form.html', {'form': form})

def marine_engineering_update(request, pk):
    marine_engineer = get_object_or_404(MarineEngineering, pk=pk)
    if request.method == 'POST':
        form = MarineEngineeringForm(request.POST, request.FILES, instance=marine_engineer)
        if form.is_valid():
            form.save()
            return redirect('marine_engineering_list')
    else:
        form = MarineEngineeringForm(instance=marine_engineer)
    return render(request, 'admin_panel/marine_engineering_form.html', {'form': form})

def marine_engineering_delete(request, pk):
    marine_engineer = get_object_or_404(MarineEngineering, pk=pk)
    if request.method == 'POST':
        marine_engineer.delete()
        return redirect('marine_engineering_list')
    return render(request, 'admin_panel/marine_engineering_confirm_delete.html', {'marine_engineer': marine_engineer})