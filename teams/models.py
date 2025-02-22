from django.db import models

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('President', 'President'),
        ('Head Officer', 'Head Officer'),
        ('Manager', 'Manager'),
        ('Supervisor', 'Supervisor'),
        ('Lead Engineer', 'Lead Engineer'),
    ]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')  # Images will be stored in 'media/team_images/'
    joined_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}"