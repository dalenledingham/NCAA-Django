from django.shortcuts import render
from .models import Conference

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