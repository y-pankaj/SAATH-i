from django.shortcuts import render
from main.models import PersonFound

def KeralaFloods(request):
    template_name = 'keralafloods.html'
    KF = PersonFound.objects.filter(disaster='Kerala_Floods')

    context = {'KF_data':KF}
    return render(request, template_name, context)

def HurricaneMichael(request):
    template_name = 'hurricane_michael.html'
    HM = PersonFound.objects.filter(disaster='HM')
    context = {'HM_data': HM}
    return render(request, template_name, context)

def CycloneTitli(request):
    template_name = ''
    return render(request, template_name)

def IndonesianTsunami(request):
    template_name = ''
    return render(request, template_name)