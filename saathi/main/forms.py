from django import forms
from .models import Feedback_form

class Feedback(forms.ModelForm):
    sender = forms.EmailField()
    message = forms.CharField()


    class Meta:
        model = Feedback_form
        fields = ('sender', 'message')