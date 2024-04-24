from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def rental_requirements(request):
    return render(request, 'rental_requirements.html')

def available_units(request):
    return render(request, 'available_units.html')

def rental_application(request):
    return render(request, 'rental_application.html')

def contact_us(request):
    return render(request, 'contact_us.html')