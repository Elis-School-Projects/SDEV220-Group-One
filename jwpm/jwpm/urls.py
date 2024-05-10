from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views

urlpatterns = [
    # Django Admin URLs
    path('admin/', admin.site.urls),

    # JWPM URLs
    path("", include("mainsite.urls")),

    # Account Management URLs
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]
