from django.shortcuts import render, redirect, get_object_or_404
from .models import Conference, Team, Player
from .forms import ConferenceForm, TeamForm, PlayerForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
  """The home page for final project"""
  return render(request, 'ncaa/index.html')

@login_required
def conferences(request):
  """Show all conferences"""
  conferences = Conference.objects.filter(owner=request.user).order_by('name')
  context = {'conferences': conferences}
  return render(request, 'ncaa/conferences.html', context)

@login_required
def conference(request, conference_id):
  """Show a single conference and all its teams"""
  conference = get_object_or_404(Conference, id=conference_id)
  # Make sure the conference belongs to the current user
  if conference.owner != request.user:
    raise Http404

  teams = conference.team_set.order_by('name')
  context = {'conference': conference, 'teams': teams}
  return render(request, 'ncaa/conference.html', context)

@login_required
def teams(request):
  """Show all teams"""
  teams = Team.objects.filter(owner=request.user).order_by('name')
  context = {'teams': teams}
  return render(request, 'ncaa/teams.html', context)

@login_required
def team(request, team_id):
  """Show a single team and all its players"""
  team = get_object_or_404(Team, id=team_id)
  # Make sure the team belongs to the current user
  if team.owner != request.user:
    raise Http404

  players = team.player_set.order_by('name')
  context = {'team': team, 'players': players}
  return render(request, 'ncaa/team.html', context)

@login_required
def players(request):
  """Show all players"""
  players = Player.objects.filter(owner=request.user).order_by('team', 'name')
  context = {'players': players}
  return render(request, 'ncaa/players.html', context)

@login_required
def player(request, player_id):
  """Show a single player"""
  player = get_object_or_404(Player, id=player_id)
  # Make sure the player belongs to the current user
  if player.owner != request.user:
    raise Http404

  context = {'player': player}
  return render(request, 'ncaa/player.html', context)

@login_required
def new_conference(request):
  """Add a new conference"""
  if request.method != 'POST':
    # No data submitted; create a blank form
    form = ConferenceForm()
  else:
    # POST data submitted; process data
    form = ConferenceForm(data=request.POST)
    if form.is_valid():
      new_conference = form.save(commit=False)
      new_conference.owner = request.user
      new_conference.save()
      return redirect('ncaa:conferences')

  # Display a blank or invalid form
  context = {'form': form}
  return render(request, 'ncaa/new_conference.html', context)

@login_required
def new_team(request, conference_id):
  """Add a new team to a particular conference"""
  conference = get_object_or_404(Conference, id=conference_id)

  if request.method != 'POST':
    # No data submitted; create a blank form
    form = TeamForm()
  else:
    # POST data submitted; process data
    form = TeamForm(data=request.POST)
    if form.is_valid():
      new_team = form.save(commit=False)
      new_team.conference = conference
      new_team.owner = request.user
      new_team.save()
      return redirect('ncaa:conference', conference_id=conference_id)

  # Display a blank or invalid form
  context = {'conference': conference, 'form': form}
  return render(request, 'ncaa/new_team.html', context)

@login_required
def new_player(request, team_id):
  """Add a new player to a particular team"""
  team = get_object_or_404(Team, id=team_id)

  if request.method != 'POST':
    # No data submitted; create a blank form
    form = PlayerForm()
  else:
    # POST data submitted; process data
    form = PlayerForm(data=request.POST)
    if form.is_valid():
      new_player = form.save(commit=False)
      new_player.team = team
      new_player.owner = request.user
      new_player.save()
      return redirect('ncaa:team', team_id=team_id)

  # Display a blank or invalid form
  context = {'team': team, 'form': form}
  return render(request, 'ncaa/new_player.html', context)

def edit_conference(request, conference_id):
  """Edit an existing conference"""
  conference = get_object_or_404(Conference, id=conference_id)
  
  if request.method != 'POST':
    # Initial request; pre-fill form with the current conference
    form = ConferenceForm(instance=conference)
  else:
    # POST data submitted; process data
    form = ConferenceForm(instance=conference, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('ncaa:conference', conference_id=conference_id)

  context = {'conference': conference, 'form': form}
  return render(request, 'ncaa/edit_conference.html', context)

def edit_team(request, team_id):
  """Edit an existing team"""
  team = get_object_or_404(Team, id=team_id)

  if request.method != 'POST':
    # Initial request; pre-fill form with the current team
    form = TeamForm(instance=team)
  else:
    # POST data submitted; process data
    form = TeamForm(instance=team, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('ncaa:team', team_id=team_id)

  context = {'team': team, 'form': form}
  return render(request, 'ncaa/edit_team.html', context)

def edit_player(request, player_id):
  """Edit an existing player"""
  player = get_object_or_404(Player, id=player_id)

  if request.method != 'POST':
    # Initial request; pre-fill form with current player
    form = PlayerForm(instance=player)
  else:
    # POST data submitted; process data
    form = PlayerForm(instance=player, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('ncaa:player', player_id=player_id)

  context = {'player': player, 'form': form}
  return render(request, 'ncaa/edit_player.html', context)

def delete_conference(request, pk):
  """Delete an existing conference"""
  conference = get_object_or_404(Conference, pk=pk)

  if request.method == 'POST':
    conference.delete()
    return redirect('/')

  return render(request, '/', {'conference': conference})

def delete_team(request, pk):
  """Delete an existing team"""
  team = get_object_or_404(Team, pk=pk)

  if request.method == 'POST':
    team.delete()
    return redirect('/')

  return render(request, '/', {'team': team})

def delete_player(request, pk):
  """Delete an existing player"""
  player = get_object_or_404(Player, pk=pk)

  if request.method == 'POST':
    player.delete()
    return redirect('/')

  return render(request, '/', {'player': player})