from django.db import models

# Ship Building Order Model
class ShipBuildingOrder(models.Model):
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Budget/Amount")
    preferred_technology = models.CharField(max_length=100, verbose_name="Preferred Shipbuilding Technology")
    ship_type = models.CharField(max_length=50, verbose_name="Ship Type")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.ship_type} with budget {self.budget}"

# Ship Repair Complaint Model
class ShipRepairComplaint(models.Model):
    ship_model = models.CharField(max_length=100, verbose_name="Ship Model")
    year_of_manufacture = models.PositiveIntegerField(verbose_name="Year of Manufacture")
    ship_type = models.CharField(max_length=50, verbose_name="Ship Type")
    issue_description = models.TextField(verbose_name="Description of the Issue")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repair Complaint for {self.ship_model}"

# Marine Engineering Faculty Model
class MarineEngineering(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    expertise = models.TextField()
    experience = models.IntegerField()
    contact_email = models.EmailField()
    profile_picture = models.ImageField(upload_to='marine_engineering/', blank=True, null=True)

    def __str__(self):
        return self.name

# Financial Report Model
class FinancialReport(models.Model):
    title = models.CharField(max_length=200, verbose_name="Report Title")
    file = models.FileField(upload_to="financial_reports/", verbose_name="Report File")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Facility Model
class Facility(models.Model):
    name = models.CharField(max_length=100, verbose_name="Facility Name")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name