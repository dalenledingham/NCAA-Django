from django import forms

from .models import Conference, Team, Player

class ConferenceForm(forms.ModelForm):
  class Meta:
    model = Conference
    fields = ['name']
    labels = {'name': 'Conference Name'}


class TeamForm(forms.ModelForm):
  class Meta:
    model = Team
    fields = ['name']
    labels = {'name': 'Team Name'}


class PlayerForm(forms.ModelForm):
  class Meta:
    model = Player
    fields = ['name','position']
    labels = {'name': 'Name','position': 'Position'}