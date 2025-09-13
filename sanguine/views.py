# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# views.py

class Mood:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Mood instances
moods = [
    Mood('Lolo', 'tabby', 'Kinda rude.', 3),
    Mood('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Mood('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Mood('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# views.py

def moods_index(request):
    # Render the cats/index.html template with the moods' data
    return render(request, 'moods/index.html', {'moods': moods})

