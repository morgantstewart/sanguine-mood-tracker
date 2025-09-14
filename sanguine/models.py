from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


MOOD_CHOICES = [
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('depressed', 'Depressed'),
    ('good', 'Good'),
    ('okay', 'Okay'),
    ('irritated', 'Irritated'),
    ('mad', 'Mad'),
    ('ecstatic', 'Ecstatic'),
]

class Mood(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    date = models.DateField(default=timezone.now, help_text="Select the date for this mood")
    mood_type = models.CharField(max_length=20, choices=MOOD_CHOICES, default='happy', help_text="Select your current mood")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mood-detail', kwargs={'mood_id': self.id})


