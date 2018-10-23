from django.db import models
from datetime import datetime

class Disasters(models.Model):
    title = models.CharField(max_length=30, blank=False)
    body = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=15, blank=False)
    date_published = models.DateTimeField(default=datetime.now, blank=False)
    link = models.CharField(max_length=100, blank=True)

class Feedback_form(models.Model):
    sender = models.EmailField()
    message = models.CharField(max_length=150)

class Prediction(models.Model):
    title = models.CharField(max_length=30, blank=False)
    body = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=100, blank=True)

class PersonFound(models.Model):
    my_choices = (
        ("KL","Kerala Floods"),
        ("HM","Hurrincane Micheal"),
        ("CT","Cyclone Titli"),
        ("IT","Indonesian Tsunami"),
    )
    contact = models.CharField(max_length=12, blank=True)
    disaster = models.CharField(max_length=50, blank=False, default='KL', choices=my_choices)
    address = models.CharField(max_length=255, blank=False)
    photo = models.ImageField(upload_to='found/', blank=False)
    uploaded_on = models.DateTimeField(auto_now_add=True)