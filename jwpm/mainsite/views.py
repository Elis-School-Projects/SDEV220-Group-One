from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Unit
from .forms import ApplicationForm, UnitForm

# Landing - Front End Page
def main(request):
    return render(request, 'main.html')

# Rental Requirements - Front End Page
def rental_requirements(request):
    return render(request, 'rental_requirements.html')

# Available Units - Front End Page
def available_units(request):
    units = Unit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'available_units.html', {'units': units})

# Rental Application - Front End Page
def rental_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('application_success')
    else:
        form = ApplicationForm()
    return render(request, 'rental_application.html', {'form': form})

# Rental Application - Successful Submit
def application_success(request):
    return render(request, 'rental_application.html', {'submit': True})

# Contact Information - Front End Page
def contact_us(request):
    return render(request, 'contact_us.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')