from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


MOOD_CHOICES = [
    ('depressed', 'Depressed'),
    ('sad', 'Sad'),
    ('okay', 'Okay'),
    ('good', 'Good'),
    ('happy', 'Happy'),
    ('ecstatic', 'Ecstatic'),
    ('irritated', 'Irritated'),
    ('mad', 'Mad'),
]

class Mood(models.Model):
    name = models.CharField(max_length=100, default="My Mood")
    description = models.TextField(max_length=250)
    date = models.DateField(default=timezone.now, help_text="Select the date for this mood")
    mood_type = models.CharField(max_length=20, choices=MOOD_CHOICES, default='happy', help_text="Select your current mood")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_mood_text(self):
        """Return emoji for each mood type"""
        mood_texts = {
            'depressed': '😔',
            'sad': '😢',
            'okay': '😐',
            'good': '😊',
            'happy': '😄',
            'ecstatic': '🤩',
            'irritated': '😤',
            'mad': '😡',
        }
        return mood_texts.get(self.mood_type, '😐')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mood-detail', kwargs={'mood_id': self.id})


