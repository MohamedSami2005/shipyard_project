from django.shortcuts import render, redirect
from .models import FAQ
from .forms import GrievanceForm

def vigilance_guidelines(request):
    return render(request, 'vigilance/guidelines.html')

def report_issue(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vigilance_thanks')
    else:
        form = GrievanceForm()
    return render(request, 'vigilance/report_issue.html', {'form': form})

def vigilance_faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'vigilance/faq.html', {'faqs': faqs})

def vigilance_thanks(request):
    return render(request, 'vigilance/thanks.html')