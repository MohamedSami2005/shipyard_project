from django.contrib import admin
from .models import Tender, Bid, Subscriber

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline', 'status')
    search_fields = ('name', 'status')

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'tender', 'bid_amount', 'submitted_at')
    search_fields = ('company_name', 'tender__name')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'subscribed_at')
    search_fields = ('email', 'phone')