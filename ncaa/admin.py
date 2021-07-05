from django.contrib import admin

# Register your models here.
from .models import Conference, Team, Player

admin.site.register(Conference)
admin.site.register(Team)
admin.site.register(Player)