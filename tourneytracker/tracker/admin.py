from django.contrib import admin
from .models import Player, Tournament, Division, Division_Type, Team, Tournament_Locations, Status, Outcome, Court, Location, Match
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Configure Import_Export models
class MatchResource(resources.ModelResource):
    team = fields.Field(
        column_name='team',
        attribute='team',
        widget=ForeignKeyWidget(Team, field='team_name')
    )
    location = fields.Field(
        column_name='location',
        attribute='location',
        widget=ForeignKeyWidget(Location, field='abbreviation')
    )
    court = fields.Field(
        column_name='court',
        attribute='court',
        widget=ForeignKeyWidget(Court, field='court_name')
    )
    status = fields.Field(
        column_name='status',
        attribute='status',
        widget=ForeignKeyWidget(Status, field='status_name')
    )
    outcome = fields.Field(
        column_name='outcome',
        attribute='outcome',
        widget=ForeignKeyWidget(Outcome, field='outcome_name')
    )
    division = fields.Field(
        column_name='division',
        attribute='division',
        widget=ForeignKeyWidget(Division, field='div_name')
    )

    class Meta:
        model = Match
        # fields = ('id', 'team', 'location')

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