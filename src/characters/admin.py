from django.contrib import admin
from characters.models import Character, Phase, Skill, Stunt, Power

# Register your models here.

admin.site.register(Character)
admin.site.register(Phase)
admin.site.register(Skill)
admin.site.register(Stunt)
admin.site.register(Power)
