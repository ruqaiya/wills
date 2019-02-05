from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import lawOffice, Lawyer, Administrator
from .forms import lawOfficeForm, LawyerForm, AdministratorForm


class lawOfficeListView(ListView):
    model = lawOffice


class lawOfficeCreateView(CreateView):
    model = lawOffice
    form_class = lawOfficeForm


class lawOfficeDetailView(DetailView):
    model = lawOffice


class lawOfficeUpdateView(UpdateView):
    model = lawOffice
    form_class = lawOfficeForm


class LawyerListView(ListView):
    model = Lawyer


class LawyerCreateView(CreateView):
    model = Lawyer
    form_class = LawyerForm


class LawyerDetailView(DetailView):
    model = Lawyer


class LawyerUpdateView(UpdateView):
    model = Lawyer
    form_class = LawyerForm


class AdministratorListView(ListView):
    model = Administrator


class AdministratorCreateView(CreateView):
    model = Administrator
    form_class = AdministratorForm


class AdministratorDetailView(DetailView):
    model = Administrator


class AdministratorUpdateView(UpdateView):
    model = Administrator
    form_class = AdministratorForm

