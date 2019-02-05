from django.contrib import admin
from django import forms
from .models import lawOffice, Lawyer, Administrator

# class lawOfficeAdminForm(forms.ModelForm):

#     class Meta:
#         model = lawOffice
#         fields = '__all__'


# class lawOfficeAdmin(admin.ModelAdmin):
#     form = lawOfficeAdminForm
#     list_display = ['name', 'slug', 'created', 'last_updated', 'address', 'phone', 'email']
#     readonly_fields = ['name', 'slug', 'created', 'last_updated', 'address', 'phone', 'email']

# admin.site.register(lawOffice, lawOfficeAdmin)


# class LawyerAdminForm(forms.ModelForm):

#     class Meta:
#         model = Lawyer
#         fields = '__all__'


# class LawyerAdmin(admin.ModelAdmin):
#     form = LawyerAdminForm
#     list_display = ['name', 'slug', 'created', 'last_updated']
#     readonly_fields = ['name', 'slug', 'created', 'last_updated']

# admin.site.register(Lawyer, LawyerAdmin)


# class AdministratorAdminForm(forms.ModelForm):

#     class Meta:
#         model = Administrator
#         fields = '__all__'


# class AdministratorAdmin(admin.ModelAdmin):
#     form = AdministratorAdminForm
#     list_display = ['name', 'slug', 'created', 'last_updated']
#     readonly_fields = ['name', 'slug', 'created', 'last_updated']

# admin.site.register(Administrator, AdministratorAdmin)

admin.site.register(lawOffice)
admin.site.register(Lawyer)
admin.site.register(Administrator)
