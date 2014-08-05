from django.forms.models import inlineformset_factory

from characters.models import Character, Phase

CharacterPhaseFormSet = inlineformset_factory(Character, Phase, can_delete=False, fields=('name', 'description', 'phase_aspect', 'guest_star', 'character'))
