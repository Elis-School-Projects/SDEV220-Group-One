from django.db import models
from django.utils import timezone
from django.conf import settings

class Unit(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Under Maintenance'),
    ]

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()  # Change to IntegerField
    rent = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def remove(self):
        self.published_date = None
        self.save()
    
class Application(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    income = models.IntegerField()
    applyingFor = models.CharField(max_length=400)
    created_date = models.DateField(default=timezone.now)   

    def __str__(self):
        return self.name