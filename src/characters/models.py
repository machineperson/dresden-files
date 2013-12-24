from django.db import models


class Phase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phase_aspect = models.CharField('Phase Aspect', max_length=300)
    guest_star = models.CharField(max_length=200, blank=True)
    
    def __unicode__(self):
        return self.name + ": " + self.phase_aspect


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
    skill_points = models.IntegerField('Skill points')
    base_refresh = models.IntegerField('Base refresh')
    notes = models.TextField(blank=True)
    inventory = models.TextField(blank=True)
    phases = models.ManyToManyField(Phase) 
    stunts = models.ManyToManyField(Stunt, blank='True')
    powers = models.ManyToManyField(Power, blank='True')
    skills = models.ManyToManyField(Skill, through='CharacterSkill')
    admin_hash = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class CharacterSkill(models.Model):
    skill = models.ForeignKey(Skill)
    character = models.ForeignKey(Character)
    rating = models.IntegerField()

    class Meta:
        ordering = ["rating"]
