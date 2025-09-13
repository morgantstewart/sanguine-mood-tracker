# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Mood


# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# views.py

class MoodData:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of MoodData instances (for fallback data)
moods_data = [
    MoodData('Lolo', 'tabby', 'Kinda rude.', 3),
    MoodData('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    MoodData('Fancy', 'bombay', 'Happy fluff ball.', 4),
    MoodData('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# views.py

def moods_index(request):
    try:
        moods = Mood.objects.all()  # Get moods from database
        # If no moods in database, use fallback data
        if not moods.exists():
            moods = moods_data
    except Exception:
        # If there's any database error, use fallback data
        moods = moods_data
    return render(request, 'moods/index.html', {'moods': moods})

def mood_detail(request, mood_id):
    try:
        mood = Mood.objects.get(id=mood_id)
    except Mood.DoesNotExist:
        # If mood doesn't exist in database, create a fallback
        mood = moods_data[mood_id - 1] if mood_id <= len(moods_data) else None
    return render(request, 'moods/detail.html', {'mood': mood})

