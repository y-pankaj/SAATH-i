from django.shortcuts import render
from main.models import PersonFound

def KeralaFloods(request):
    template_name = 'Found/kerala_floods.html'
    HM = PersonFound.objects.filter(disaster='KL')

    context = {'HM_data':HM}
    return render(request, template_name, context)

def HurricaneMichael(request):
    template_name = 'Found/hurricane_michael.html'
    HM = PersonFound.objects.filter(disaster='HM')
    context = {'HM_data': HM}
    return render(request, template_name, context)

def CycloneTitli(request):
    template_name = 'Found/cyclone_titli.html'
    HM = PersonFound.objects.filter(disaster='CT')
    context = {'HM_data': HM}
    return render(request, template_name, context)

def IndonesianTsunami(request):
    template_name = 'Found/indonesian_tsunami.html'
    HM = PersonFound.objects.filter(disaster='IT')
    context = {'HM_data': HM}
    return render(request, template_name, context)