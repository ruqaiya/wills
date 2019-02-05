from django.contrib import admin
from django import forms
from .models import ClientSession, Client, Spouse, Child

# class ClientSessionAdminForm(forms.ModelForm):

#     class Meta:
#         model = ClientSession
#         fields = '__all__'


# class ClientSessionAdmin(admin.ModelAdmin):
#     form = ClientSessionAdminForm
#     list_display = ['created', 'last_updated']
#     readonly_fields = ['created', 'last_updated']

# admin.site.register(ClientSession, ClientSessionAdmin)


# class ClientAdminForm(forms.ModelForm):

#     class Meta:
#         model = Client
#         fields = '__all__'


# class ClientAdmin(admin.ModelAdmin):
#     form = ClientAdminForm
#     list_display = ['name', 'slug', 'created', 'last_updated', 'occupation', 'address', 'home_telephone', 'work_telephone', 'domicile', 'dob', 'place_of_birth', 'name_at_birth', 'marital_status']
#     readonly_fields = ['name', 'slug', 'created', 'last_updated', 'occupation', 'address', 'home_telephone', 'work_telephone', 'domicile', 'dob', 'place_of_birth', 'name_at_birth', 'marital_status']

# admin.site.register(Client, ClientAdmin)


# class SpouseAdminForm(forms.ModelForm):

#     class Meta:
#         model = Spouse
#         fields = '__all__'


# class SpouseAdmin(admin.ModelAdmin):
#     form = SpouseAdminForm
#     list_display = ['name', 'slug', 'created', 'last_updated', 'domicile', 'dob', 'place_of_birth', 'dom', 'place_of_marriage', 'marriage_contract_exists', 'marriage_contract', 'seperated', 'divorced', 'dos', 'dod', 'divorce_contract']
#     readonly_fields = ['name', 'slug', 'created', 'last_updated', 'domicile', 'dob', 'place_of_birth', 'dom', 'place_of_marriage', 'marriage_contract_exists', 'marriage_contract', 'seperated', 'divorced', 'dos', 'dod', 'divorce_contract']

# admin.site.register(Spouse, SpouseAdmin)


# class ChildAdminForm(forms.ModelForm):

#     class Meta:
#         model = Child
#         fields = '__all__'


# class ChildAdmin(admin.ModelAdmin):
#     form = ChildAdminForm
#     list_display = ['name', 'slug', 'created', 'last_updated', 'dob', 'live_in', 'address', 'notes', 'custody', 'adopted', 'legitimate']
#     readonly_fields = ['name', 'slug', 'created', 'last_updated', 'dob', 'live_in', 'address', 'notes', 'custody', 'adopted', 'legitimate']

# admin.site.register(Child, ChildAdmin)


admin.site.register(Client)
admin.site.register(ClientSession)
admin.site.register(Spouse)
admin.site.register(Child)
