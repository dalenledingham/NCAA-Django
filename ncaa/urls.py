"""Defines URL patterns for ncaa"""

from django.urls import path
from . import views

app_name = 'ncaa'
urlpatterns = [
  # Home page
  path('', views.index, name='index'),

  # Page that shows all conferences
  path('conferences/', views.conferences, name='conferences'),

  # Details page for a single conference
  path('conferences/<int:conference_id>/', views.conference, name='conference'),

  # Page that shows all teams
  path('teams/', views.teams, name='teams'),

  # Details page for a single team
  path('teams/<int:team_id>/', views.team, name='team'),

  # Page that shows all players
  path('players/', views.players, name='players'),

  # Details page for a single player
  path('players/<int:player_id>/', views.player, name="player"),

  # Page for adding a new Conference
  path('new_conference/', views.new_conference, name='new_conference'),

  # Page for adding a new Team
  path('new_team/<int:conference_id>/', views.new_team, name='new_team'),

  # Page for adding a new Player
  path('new_player/<int:team_id>/', views.new_player, name='new_player'),

  # Page for editing a conference
  path('edit_conference/<int:conference_id>/', views.edit_conference, name='edit_conference'),

  # Page for editing a team
  path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),
]