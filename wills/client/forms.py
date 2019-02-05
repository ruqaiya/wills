from django import forms
from .models import ClientSession, Client, Spouse, Child


class ClientSessionForm(forms.ModelForm):
    class Meta:
        model = ClientSession
        fields = ['client']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'occupation', 'address', 'home_telephone', 'work_telephone', 'domicile', 'dob', 'place_of_birth', 'name_at_birth', 'marital_status']


class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = ['name', 'domicile', 'dob', 'place_of_birth', 'dom', 'place_of_marriage', 'marriage_contract_exists', 'marriage_contract', 'seperated', 'divorced', 'dos', 'dod', 'divorce_contract', 'session']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'dob', 'live_in', 'address', 'notes', 'custody', 'adopted', 'legitimate', 'session']


