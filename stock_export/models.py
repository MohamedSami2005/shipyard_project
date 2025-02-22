# stock_export/models.py
from django.db import models
from django.contrib.auth.models import User  # Import the User model

class StockExportRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Add this line
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    stock_name = models.CharField(max_length=100)
    stock_category = models.CharField(max_length=50)
    stock_quantity = models.FloatField()
    stock_value = models.FloatField()
    stock_condition = models.CharField(max_length=50)
    stock_images = models.ImageField(upload_to='stock_images/')
    destination_country = models.CharField(max_length=100)
    destination_port = models.CharField(max_length=100)
    expected_delivery_date = models.DateField()
    mode_of_transport = models.CharField(max_length=50)
    warehouse_location = models.CharField(max_length=100)
    shipping_partner = models.CharField(max_length=100, blank=True, null=True)
    export_license_required = models.BooleanField(default=False)
    customs_declaration_form = models.FileField(upload_to='customs_docs/')
    special_handling_instructions = models.TextField(blank=True, null=True)
    payment_mode = models.CharField(max_length=50)
    insurance_required = models.BooleanField(default=False)
    insurance_documents = models.FileField(upload_to='insurance_docs/', blank=True, null=True)
    terms_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock_name} - {self.full_name}"