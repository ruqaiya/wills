from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def home(request):
    return render(request, 'home.html')
