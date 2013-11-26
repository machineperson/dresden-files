from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    template = models.CharField(max_length=100)
    high_concept = models.CharField('High Concept', max_length=100)
    trouble = models.CharField('Trouble Aspect', max_length=100)
    skill_points = models.IntegerField('Skill points')
    base_refresh = models.IntegerField('Base refresh')
    notes = models.TextField()
    inventory = models.TextField() 
    
    def __unicode__(self):
        return self.name


class Phase(models.Model):
    character = models.ManyToManyField(Character)    
    name = models.CharField(max_length=100)
    description = models.TextField()
    phase_aspect = models.CharField('Phase Aspect', max_length=300)
    guest_star = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name + ": " + self.phase_aspect

class Stunt(models.Model):
    character = models.ManyToManyField(Character)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Power(models.Model):
    character = models.ManyToManyField(Character)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Skill(models.Model):
    character = models.ManyToManyField(Character, through='CharacterSkill')
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class CharacterSkill(models.Model):
    character = models.ForeignKey(Character)
    skill = models.ForeignKey(Skill)
    rating = models.IntegerField()
