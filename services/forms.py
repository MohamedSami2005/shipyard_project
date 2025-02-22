from django import forms
from .models import ShipBuildingOrder, ShipRepairComplaint
from .models import MarineEngineering

class ShipBuildingOrderForm(forms.ModelForm):
    class Meta:
        model = ShipBuildingOrder
        fields = ['budget', 'preferred_technology', 'ship_type']

class ShipRepairComplaintForm(forms.ModelForm):
    class Meta:
        model = ShipRepairComplaint
        fields = ['ship_model', 'year_of_manufacture', 'ship_type', 'issue_description']

class MarineEngineeringForm(forms.ModelForm):
    class Meta:
        model = MarineEngineering
        fields = ['name', 'designation', 'expertise', 'experience', 'contact_email', 'profile_picture']
