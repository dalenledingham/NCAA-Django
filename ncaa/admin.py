from django.contrib import admin

# Register your models here.
from .models import Conference, Team

admin.site.register(Conference)
admin.site.register(Team)