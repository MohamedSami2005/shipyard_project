# stock_export/forms.py
from django import forms
from .models import StockExportRequest

class StockExportForm(forms.ModelForm):
    class Meta:
        model = StockExportRequest
        fields = '__all__'