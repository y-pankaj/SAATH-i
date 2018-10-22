from django.shortcuts import render, redirect
from main.models import Disasters
from .forms import Feedback
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

def HomePageView(request):
    template_name = 'index.html'
    context = {'disasters': Disasters.objects.all()}
    return render(request, template_name, context)

def AboutView(request):
    template_name = 'about.html'
    return render(request, template_name)


def ContactView(request):
    if request.method == 'POST':
        form = Feedback(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            f_message = form.cleaned_data['message']
            post = form.save(commit=False)

            # ........Sending the email.......
            subject = 'Your response'
            from_email = settings.EMAIL_HOST_USER
            message = 'We have received your query'  # TODO update feedback message to user
            to_list = [sender]
            send_mail(subject, message, from_email, to_list, fail_silently=False)

            subject = 'Feedback from {}'.format(sender)
            from_email = settings.EMAIL_HOST_USER
            message = f_message  # TODO update feedback message to user
            to_list = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=False)

            return redirect('contact')
    else:
        form = Feedback()
        template_name = 'contact.html'

    return render(request, template_name, {'form': form})

def PredictionsView(request):
    template_name = 'predictions.html'
    return render(request, template_name)