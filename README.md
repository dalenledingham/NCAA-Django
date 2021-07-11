# NCAA-Django

This Django application allows registered users to build their own NCAA college football league. 

Leagues are split into collections of teams, called conferences, and each team consists of any number of players. Users can create new conferences, teams, and players, and may structure their league however they wish. 

Users must create their league from the top level down, i.e., conferences must be created before teams, and teams must be created before players. When creating a new team or player, the new object will be automatically assigned to the selected conference or team respectively regardless of the choice in the dropdown menu. 

Link: https://ncaa-django.herokuapp.com/