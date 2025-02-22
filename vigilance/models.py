from django.db import models

class Grievance(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    contact_details = models.CharField(max_length=100, blank=True, null=True)
    COMPLAINT_TYPES = [
        ('Fraud', 'Fraud'),
        ('Corruption', 'Corruption'),
        ('Safety Violation', 'Safety Violation'),
        ('Harassment', 'Harassment'),
        ('Other', 'Other'),
    ]
    complaint_type = models.CharField(max_length=50, choices=COMPLAINT_TYPES)
    description = models.TextField()
    evidence = models.FileField(upload_to='grievance_evidence/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grievance by {self.name or 'Anonymous'} on {self.submitted_at}"

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question