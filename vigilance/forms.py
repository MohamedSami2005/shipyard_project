from django import forms
from .models import Grievance

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['name', 'contact_details', 'complaint_type', 'description', 'evidence']