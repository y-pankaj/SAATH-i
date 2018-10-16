from django.shortcuts import render
from django.views import generic
from django.views.generic import View
# Create your views here.

def HomePageView(request):
    template_name = 'index.html'
    return render(request, template_name)

def AboutView(request):
    template_name = 'about.html'
    return render(request, template_name)

def ContactView(request):
    template_name = 'contact.html'
    return render(request, template_name)

def PredictionsView(request):
    template_name = 'predictions.html'
    return render(request, template_name)