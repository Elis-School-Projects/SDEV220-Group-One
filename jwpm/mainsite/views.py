from django.shortcuts import render
from django.utils import timezone
from .models import Unit

def main(request):
    return render(request, 'main.html')

def rental_requirements(request):
    return render(request, 'rental_requirements.html')

def available_units(request):
    units = Unit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'available_units.html', {'units': units})

def rental_application(request):
    return render(request, 'rental_application.html')

def contact_us(request):
    return render(request, 'contact_us.html')