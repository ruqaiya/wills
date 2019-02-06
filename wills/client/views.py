from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import ClientSession, Client, Spouse, Child
from .forms import ClientSessionForm, ClientForm, SpouseForm, ChildForm
from mailmerge import MailMerge
from django.http import HttpResponse
from docxtpl import DocxTemplate

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


def generateDoc(request):
    template = "templates/will_templates/dummy.docx"

    document = MailMerge(template)
    print("printing things")
    print(document.get_merge_fields())
    document.merge({
        'full_name': 'Abc Something',
        'address': "1300, Yates Street",
        'spouse_name': "Def Something",
        'spouse_address': "1301 Yates Street"
    })
    document.write('test-output.docx')

    return HttpResponse("Aparently the doc is created!")

def generateDoc2(request):
    doc = DocxTemplate("templates/will_templates/dummy2.docx")
    context = {
        'full_name': 'Abc Something',
        'address': "1300, Yates Street",
        'spouse_name': "Def Something",
        'spouse_address': "1301 Yates Street"
    }
    doc.render(context)
    doc.save("generated_doc.docx")

    return HttpResponse("Aparently the doc is created!")