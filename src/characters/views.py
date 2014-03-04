from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from characters.models import Character

def index(request):
    return HttpResponse("Hello, world!")

class CharacterView(generic.DetailView):
    model = Character
    fields = ['name', 'description', 'template', 'high_concept', 'trouble', 'skill_points', 'base_refresh', 'skill_cap', 'notes', 'inventory']
    template_name = 'characters/display_character.html'

class CharacterCreateView(generic.CreateView):
    model = Character
    fields = ['name', 'description', 'template', 'high_concept', 'trouble', 'skill_points', 'base_refresh', 'skill_cap', 'notes', 'inventory']
    template_name = 'characters/create_character.html'
    success_url = reverse('character_created', kwargs={'pk': self._id, 'view_hash': self.view_hash, 'admin_hash': self.admin_hash}

class CSkillsEditView(generic.UpdateView):
    model = Character
    fields = ['skills']
    template_name = 'characters/edit_skills.html' 
