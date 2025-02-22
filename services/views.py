from django.shortcuts import render, redirect
from .models import ShipBuildingOrder, ShipRepairComplaint, MarineEngineering, FinancialReport, Facility
from .forms import ShipBuildingOrderForm, ShipRepairComplaintForm

# Ship Building View
def ship_building(request):
    if request.method == 'POST':
        form = ShipBuildingOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ship_building_thanks')  # Redirect to the thank-you page
    else:
        form = ShipBuildingOrderForm()
    return render(request, 'services/ship_building.html', {'form': form})

# Ship Repair View
def ship_repair(request):
    form_submitted = False  # Initialize the flag

    if request.method == 'POST':
        form = ShipRepairComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            form_submitted = True  # Corrected variable name
            return render(request, 'services/ship_repair.html', {'form': form, 'form_submitted': form_submitted})
    else:
        form = ShipRepairComplaintForm()

    return render(request, 'services/ship_repair.html', {'form': form, 'form_submitted': form_submitted})

# Marine Engineering View
def marine_engineering(request):
    faculty = MarineEngineering.objects.all()
    return render(request, 'services/marine_engineering.html', {'faculty': faculty})

# Financials View
def financials(request):
    reports = FinancialReport.objects.all()
    return render(request, 'services/financials.html', {'reports': reports})

# Facilities View
def facilities(request):
    facilities = Facility.objects.all()
    return render(request, 'services/facilities.html', {'facilities': facilities})

def ship_building_thanks(request):
    return render(request, 'services/ship_building_thanks.html')