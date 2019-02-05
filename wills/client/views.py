from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import ClientSession, Client, Spouse, Child
from .forms import ClientSessionForm, ClientForm, SpouseForm, ChildForm


class ClientSessionListView(ListView):
    model = ClientSession


class ClientSessionCreateView(CreateView):
    model = ClientSession
    form_class = ClientSessionForm


class ClientSessionDetailView(DetailView):
    model = ClientSession


class ClientSessionUpdateView(UpdateView):
    model = ClientSession
    form_class = ClientSessionForm


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm


class SpouseListView(ListView):
    model = Spouse


class SpouseCreateView(CreateView):
    model = Spouse
    form_class = SpouseForm


class SpouseDetailView(DetailView):
    model = Spouse


class SpouseUpdateView(UpdateView):
    model = Spouse
    form_class = SpouseForm


class ChildListView(ListView):
    model = Child


class ChildCreateView(CreateView):
    model = Child
    form_class = ChildForm


class ChildDetailView(DetailView):
    model = Child


class ChildUpdateView(UpdateView):
    model = Child
    form_class = ChildForm

