from django import forms

from .models import Unit, Application

# For Manager Dashboard to add new or edit units on the Available Units page
class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('address', 'status', 'bedrooms', 'bathrooms', 'rent',)

# For anyone using the site to submit a rental application
class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name', 'email', 'phone', 'income', 'applyingFor',)