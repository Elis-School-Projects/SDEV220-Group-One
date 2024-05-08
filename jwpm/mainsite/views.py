from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Unit, Application
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
# def dashboard(request):
#     # Fetch all applications from the database
#     applications = Application.objects.all()
    
#     # Pass the applications to the template
#     return render(request, 'dashboard.html', {'applications': applications})
def dashboard(request):
    applications = Application.objects.all()
    units = Unit.objects.all()
    return render(request, 'dashboard.html', {'applications': applications, 'units': units})

@login_required
def delete_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == 'POST':
        application.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete_application.html', {'application': application})

@login_required
def post_unit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UnitForm()
    return render(request, 'post_unit.html', {'form': form})
    
@login_required
def edit_unit(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UnitForm(instance=unit)
    return render(request, 'edit_unit.html', {'form': form, 'unit': unit})

@login_required
def delete_unit(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    if request.method == 'POST':
        unit.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete_unit.html', {'unit': unit})