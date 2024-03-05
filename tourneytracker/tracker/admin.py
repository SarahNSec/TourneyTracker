from django.contrib import admin
from .models import Player, Tournament, Division, Division_Type, Team, Tournament_Locations, Status, Outcome, Court, Location, Match

# Register your models here.
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Division)
admin.site.register(Division_Type)
admin.site.register(Team)
admin.site.register(Tournament_Locations)
admin.site.register(Status)
admin.site.register(Outcome)
admin.site.register(Court)
admin.site.register(Location)
admin.site.register(Match)