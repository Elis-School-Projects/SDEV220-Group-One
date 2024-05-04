from django.db import models
from django.utils import timezone
from django.conf import settings

class Unit(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    status = models.TextField()
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    rent = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def remove(self):
        self.published_date = None
        self.save()

    def __str__(self):
        return self.address
    
class Unit(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    phone = models.TextField()
    income = models.IntegerField()
    applyingFor = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name