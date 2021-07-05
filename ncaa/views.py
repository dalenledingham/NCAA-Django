from django.shortcuts import render
from .models import Conference, Team

# Create your views here.
def index(request):
  """The home page for final project"""
  return render(request, 'ncaa/index.html')

def conferences(request):
  """Show all conferences"""
  conferences = Conference.objects.order_by('name')
  context = {'conferences': conferences}
  return render(request, 'ncaa/conferences.html', context)

def conference(request, conference_id):
  """Show a single conference and all its teams"""
  conference = Conference.objects.get(id=conference_id)
  teams = conference.team_set.order_by('name')
  context = {'conference': conference, 'teams': teams}
  return render(request, 'ncaa/conference.html', context)

def teams(request):
  """Show all teams"""
  teams = Team.objects.order_by('name')
  context = {'teams': teams}
  return render(request, 'ncaa/teams.html', context)

def team(request, team_id):
  """Show a single team and all its players"""
  team = Team.objects.get(id=team_id)
  players = team.player_set.order_by('name')
  context = {'team': team, 'players': players}
  return render(request, 'ncaa/team.html', context)