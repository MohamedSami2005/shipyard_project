# Generated by Django 5.1.5 on 2025-02-22 04:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockExportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('stock_name', models.CharField(max_length=100)),
                ('stock_category', models.CharField(max_length=50)),
                ('stock_quantity', models.FloatField()),
                ('stock_value', models.FloatField()),
                ('stock_condition', models.CharField(max_length=50)),
                ('stock_images', models.ImageField(upload_to='stock_images/')),
                ('destination_country', models.CharField(max_length=100)),
                ('destination_port', models.CharField(max_length=100)),
                ('expected_delivery_date', models.DateField()),
                ('mode_of_transport', models.CharField(max_length=50)),
                ('warehouse_location', models.CharField(max_length=100)),
                ('shipping_partner', models.CharField(blank=True, max_length=100, null=True)),
                ('export_license_required', models.BooleanField(default=False)),
                ('customs_declaration_form', models.FileField(upload_to='customs_docs/')),
                ('special_handling_instructions', models.TextField(blank=True, null=True)),
                ('payment_mode', models.CharField(max_length=50)),
                ('insurance_required', models.BooleanField(default=False)),
                ('insurance_documents', models.FileField(blank=True, null=True, upload_to='insurance_docs/')),
                ('terms_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
