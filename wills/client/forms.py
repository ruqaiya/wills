from django import forms
from .models import ClientSession, Client, Spouse, Child


# Choices Values
MARRIED = 'MR'
SINGLE = 'SL'
LIVINGTOGETHER = 'LT'
MARRIED_STATUS_CHOICES = (
    (SINGLE, 'Single'),
    (MARRIED, 'Married'),
    (LIVINGTOGETHER, 'Living together')
)


class ClientSessionForm(forms.ModelForm):
    class Meta:
        model = ClientSession
        fields = ['client']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'occupation', 'address', 'home_telephone', 'work_telephone', 'domicile', 'dob', 'place_of_birth', 'name_at_birth', 'marital_status']


class ClientFormShort(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'dob', 'marital_status']


class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = ['name', 'domicile', 'dob', 'place_of_birth', 'dom', 'place_of_marriage', 'marriage_contract_exists', 'marriage_contract', 'seperated', 'divorced', 'dos', 'dod', 'divorce_contract', 'session']


class SpouseFormShort(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = ['name', 'session']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'dob', 'live_in', 'address', 'notes', 'custody', 'adopted', 'legitimate', 'session']


class ChildFormShort(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'dob', 'session']


class MarriedStatusForm(forms.Form):
    married = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        super(MarriedStatusForm, self).__init__(*args, **kwargs)
        self.fields['married'].choices = MARRIED_STATUS_CHOICES

    def save_to_session(self):
        self.request.session['married'] = self.cleaned_data['married']
        pass
