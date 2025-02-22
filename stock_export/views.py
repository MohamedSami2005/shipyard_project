# stock_export/views.py
from django.shortcuts import render, redirect
from .forms import StockExportForm

def stock_export_request(request):
    if request.method == 'POST':
        form = StockExportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stock_export_success')
    else:
        form = StockExportForm()
    return render(request, 'stock_export/request.html', {'form': form})

def stock_export_success(request):
    return render(request, 'stock_export/success.html')