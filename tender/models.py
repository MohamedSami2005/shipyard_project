from django.db import models

class Tender(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    bid_amount_range = models.CharField(max_length=100)
    document = models.FileField(upload_to='tender_documents/')
    status = models.CharField(
        max_length=20,
        choices=[
            ('Open', 'Open'),
            ('Closed', 'Closed'),
            ('Under Review', 'Under Review'),
            ('Awarded', 'Awarded'),
        ],
        default='Open',
    )

    def __str__(self):
        return self.name

class Bid(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, related_name='bids')
    company_name = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=200)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    proposal_document = models.FileField(upload_to='bid_documents/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid by {self.company_name} for {self.tender.name}"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email