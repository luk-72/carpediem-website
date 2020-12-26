from django.views.generic.base import TemplateView

from django.template import loader

from django.shortcuts import render

def index(request):
    
    return render(request, 'home.html')