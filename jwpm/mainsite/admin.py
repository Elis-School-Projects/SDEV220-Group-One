# Import Modules
from django.contrib import admin
from .models import Unit, Application

# Register DB Models in Admin Panel
admin.site.register(Unit)
admin.site.register(Application)