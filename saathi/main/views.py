from django.shortcuts import render
from main.models import Disasters


def HomePageView(request):
    template_name = 'index.html'
    context = { 'disasters' : Disasters.objects.all() }
    return render(request, template_name, context)

def AboutView(request):
    template_name = 'about.html'
    return render(request, template_name)

def ContactView(request):
    template_name = 'contact.html'
    return render(request, template_name)

def PredictionsView(request):
    template_name = 'predictions.html'
    return render(request, template_name)