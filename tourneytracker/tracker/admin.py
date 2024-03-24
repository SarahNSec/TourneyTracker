from django.contrib import admin
from .models import Player, Tournament, Division, Division_Type, Team, Tournament_Locations, Status, Outcome, Court, Location, Match
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Configure Import_Export models
class MatchResource(resources.ModelResource):

    class Meta:
        model = Match

class MatchAdmin(ImportExportModelAdmin):
    resource_classes = [MatchResource]

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
admin.site.register(Match, MatchAdmin)