from django.db import models
from datetime import datetime

class Disasters(models.Model):
    title = models.CharField(max_length=30, blank=False)
    body = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=15, blank=False)
    date_published = models.DateTimeField(default=datetime.now, blank=False)
    link = models.CharField(max_length=100, blank=True)