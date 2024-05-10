from django.urls import path

from . import views

urlpatterns = [
    # Publicly Available Pages
    path('', views.main, name='main'),
    path('rental_requirements/', views.rental_requirements, name='rental_requirements'),
    path('available_units/', views.available_units, name='available_units'),
    path('rental_application/', views.rental_application, name='rental_application'),
    path('rental_application/success/', views.application_success, name='application_success'),
    path('contact_us/', views.contact_us, name='contact_us'),
    
    # Protected Admin Routes
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete_application/<int:application_id>/', views.delete_application, name='delete_application'),
    path('post_unit/', views.post_unit, name='post_unit'),
    path('edit_unit/<int:unit_id>/', views.edit_unit, name='edit_unit'),
    path('delete_unit/<int:unit_id>/', views.delete_unit, name='delete_unit'),
]