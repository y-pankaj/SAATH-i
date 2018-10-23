from django import forms
from .models import Feedback_form
from .models import PersonFound

class Feedback(forms.ModelForm):

    class Meta:
        model = Feedback_form
        fields = ('sender', 'message')

class Found(forms.ModelForm):

    class Meta:
        model = PersonFound
        fields = ('contact', 'disaster', 'address', 'photo',)