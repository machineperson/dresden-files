from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from characters.models import Character
from django.core.urlresolvers import reverse, reverse_lazy 
from characters.forms import CharacterPhaseFormSet

import logging

logger = logging.getLogger(__name__)

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
    
    def get_success_url(self):
        return reverse('edit-phases', kwargs={'pk': self.object.pk, 'character': self.object})


class CSkillsEditView(generic.UpdateView):
    model = Character
    fields = ['skills']
    template_name = 'characters/edit_skills.html' 

class EditCharacterPhaseView(generic.UpdateView):
    model = Character
    form_class = CharacterPhaseFormSet
    template_name = "characters/edit_phases.html"

    def get_success_url(self):
        return self.get_object().get_absolute_url()
