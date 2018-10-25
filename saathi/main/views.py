from django.shortcuts import render, redirect, HttpResponse
from main.models import Disasters, Prediction
from .forms import Feedback, Found
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def HomePageView(request):
    if request.method == 'POST':
        if 'latitude' in request.POST:
            lat = request.POST['latitude']
            lon = request.POST['longitude']
            key = 'yivWcEFmJWKFvIteu_8LluM1uZgauY8oLecRRsYBqFg'
            url = 'https://atlas.microsoft.com/search/address/reverse/json?subscription-key='+key+'&api-version=1.0&query='+lat+','+lon+''
            response = requests.get(url)
            json = response.json()
            text='Latitude:' + lat + '\nLongitude:' + lon + '\nAddress:\n'
            text =text+str(json['addresses'][0]['address'])

            #content = 'Latitude:' + lat + '\nLongitude:' + lon + '\nAddress:\n'
            #content = content + text['streetName'] + ',' + text['municipalitySubdivision'] + ',' + text['municipality'] + ',' + text['country'] + '-' + text['postalCode']

            #...........SEND MAIL............
            subject = 'Distress Signal'
            from_email = settings.EMAIL_HOST_USER
            message = text  # TODO update feedback message to user
            to_list = ['pankaj2000.fideri@gmail.com']
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            return HttpResponse('success')  # if everything is OK
    template_name = 'index.html'
    return render(request, template_name)

def AboutView(request):
    template_name = 'about.html'
    return render(request, template_name)


def ContactView(request):
    if request.method == 'POST':
        form = Feedback(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            f_message = form.cleaned_data['message']
            post = form.save(commit=False)

            # ........Sending the email.......
            subject = 'Your response'
            from_email = settings.EMAIL_HOST_USER
            message = 'Thank You for giving us your valuable suggestion.'  # TODO update feedback message to user
            to_list = [sender]
            send_mail(subject, message, from_email, to_list, fail_silently=False)

            subject = 'Feedback from {}'.format(sender)
            from_email = settings.EMAIL_HOST_USER
            message = f_message  # TODO update feedback message to user
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=False)

            return redirect('main:contact')
    else:
        form = Feedback()
        template_name = 'contact.html'

    return render(request, template_name, {'form': form})

def PredictionsView(request):
    template_name = 'predictions.html'
    context = {'prediction':Prediction.objects.all()}
    return render(request, template_name,context)

def FoundView(request): # TODO Complete the found.html page Write some thing at the top. And include link of the disasters
    if request.method == 'POST':
        form = Found(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = Found()
        template_name = 'found.html'
    return render(request, template_name, {'form':form})