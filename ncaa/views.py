from django.shortcuts import render, redirect
from .models import Conference, Team
from .forms import ConferenceForm, TeamForm

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

def new_conference(request):
  """Add a new conference"""
  if request.method != 'POST':
    # No data submitted; create a blank form
    form = ConferenceForm()
  else:
    # POST data submitted; process data
    form = ConferenceForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('ncaa:conferences')

  # Display a blank or invalid form
  context = {'form': form}
  return render(request, 'ncaa/new_conference.html', context)

def new_team(request, conference_id):
  """Add a new team for a particular conference"""
  conference = Conference.objects.get(id=conference_id)

  if request.method != 'POST':
    # No data submitted; create a blank form
    form = TeamForm()
  else:
    # POST data submitted; process data
    form = TeamForm(data=request.POST)
    if form.is_valid():
      new_team = form.save(commit=False)
      new_team.conference = conference
      new_team.save()
      return redirect('ncaa:conference', conference_id=conference_id)

  # Display a blank or invalid form
  context = {'conference': conference, 'form': form}
  return render(request, 'ncaa/new_team.html', context)