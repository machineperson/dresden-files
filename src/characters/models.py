from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.db.models import F
from django.core.urlresolvers import reverse


class Stunt(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Power(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    template = models.CharField(max_length=100)
    high_concept = models.CharField('High Concept', max_length=100)
    trouble = models.CharField('Trouble Aspect', max_length=100)
    skill_points = models.PositiveIntegerField('Skill points')
    base_refresh = models.PositiveIntegerField('Base refresh')
    skill_cap = models.PositiveIntegerField('Skill cap')    
    notes = models.TextField(blank=True)
    inventory = models.TextField(blank=True)
    stunts = models.ManyToManyField(Stunt, blank=True)
    powers = models.ManyToManyField(Power, blank=True)
    skills = models.ManyToManyField(Skill, through='CharacterSkill', blank=True)
    admin_hash = models.CharField(max_length=200, editable=False)
    view_hash = models.CharField(max_length=200, editable=False)

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.pk})


    def __unicode__(self):
        return self.name

class Phase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phase_aspect = models.CharField('Phase Aspect', max_length=300)
    guest_star = models.CharField(max_length=200, blank=True)
    character = models.ForeignKey(Character)
    def __unicode__(self):
        return self.name + ": " + self.phase_aspect

class CharacterSkill(models.Model):
    skill = models.ForeignKey(Skill, validators = [MaxValueValidator(F('character.skill_cap'))])
    character = models.ForeignKey(Character)
    rating = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse('edit-skills', kwargs={'pk': self.character})

    class Meta:
        ordering = ["rating"]

def ensure_phases(sender, **kwargs):
    if kwargs.get('created', False):
        for phase in ['Background', 'Rising Conflict', 'The Story', 'Guest Star', 'Guest Star Redux']:
            Phase.objects.create(character=kwargs.get('instance'), name=phase, phase_aspect=' ')
        for s in Skill.objects.all():
            CharacterSkill.objects.create(character=kwargs.get('instance'), skill=s, rating=0)

post_save.connect(ensure_phases, sender=Character)
