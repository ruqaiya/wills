from django import forms
from .models import lawOffice, Lawyer, Administrator


class lawOfficeForm(forms.ModelForm):
    class Meta:
        model = lawOffice
        fields = ['name', 'address', 'phone', 'email']


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['name', 'user']


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['name', 'user']


