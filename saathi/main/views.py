from django.shortcuts import render, redirect
from main.models import Disasters
from .forms import Feedback

def HomePageView(request):
    template_name = 'index.html'
    context = {'disasters': Disasters.objects.all()}
    return render(request, template_name, context)

def AboutView(request):
    template_name = 'about.html'
    return render(request, template_name)

def ContactView(request):
    if request.method=='POST':
        form = Feedback(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            post = form.save(commit=False)

            # ........Sending the email.......
            return redirect('contact')
    else:
        form = Feedback()
        template_name = 'contact.html'
    return render(request, template_name, {form:'form'})

def PredictionsView(request):
    template_name = 'predictions.html'
    return render(request, template_name)