from django import forms
from .models import Bid, Subscriber

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['company_name', 'contact_details', 'bid_amount', 'proposal_document']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'phone']