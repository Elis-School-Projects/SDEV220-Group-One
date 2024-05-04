from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('rental_requirements/', views.rental_requirements, name='rental_requirements'),
    path('available_units/', views.available_units, name='available_units'),
    path('rental_application/', views.rental_application, name='rental_application'),
    path('contact_us/', views.contact_us, name='contact_us'),
]