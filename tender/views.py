from django.shortcuts import render, get_object_or_404, redirect
from .models import Tender, Bid, Subscriber
from .forms import BidForm, SubscribeForm

def tender_list(request):
    tenders = Tender.objects.filter(status='Open')
    return render(request, 'tender/tender_list.html', {'tenders': tenders})

def tender_detail(request, pk):
    tender = get_object_or_404(Tender, pk=pk)
    if request.method == 'POST':
        form = BidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.tender = tender
            bid.save()
            return redirect('tender_detail', pk=pk)
    else:
        form = BidForm()
    return render(request, 'tender/tender_detail.html', {'tender': tender, 'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tender_list')
    else:
        form = SubscribeForm()
    return render(request, 'tender/subscribe.html', {'form': form})