from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from characters.models import Character

def index(request):
    return HttpResponse("Hello, world!")

class CharacterView(generic.DetailView):
    model = Character
    template_name = 'characters/display_character.html'

class CharacterCreateView(generic.CreateView):
    model = Character
    template_name = 'characters/create_character.html'
