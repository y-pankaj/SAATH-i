from django import forms
from .models import Feedback_form

class Feedback(forms.ModelForm):

    class Meta:
        model = Feedback_form
        fields = ('sender', 'message')