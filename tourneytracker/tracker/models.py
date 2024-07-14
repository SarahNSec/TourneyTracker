from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=256)

    def __str__(self):
        return self.player_name
    
class Location(models.Model):
    location_name = models.CharField(max_length=256)
    abbreviation = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.location_name
    
class Status(models.Model):
    status_name = models.CharField(max_length=256)

    def __str__(self):
        return self.status_name
    
class Outcome(models.Model):
    outcome_name = models.CharField(max_length=256)

    def __str__(self):
        return self.outcome_name

class Tournament(models.Model):
    tourney_name = models.CharField("Tournament Name", max_length=256)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.tourney_name
    
class Division_Type(models.Model):
    div_type = models.CharField("Type", max_length=256)

    def __str__(self):
        return self.div_type
    
    
class Court(models.Model):
    court_name = models.CharField(max_length=256)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.court_name

class Tournament_Locations(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tournament}-{self.location}'
    
class Division(models.Model):
    div_name = models.CharField("Name", max_length=256)
    # div_type = models.ForeignKey(Division_Type, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.div_name

class Team(models.Model):
    team_name = models.CharField(max_length=256)
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_1_record')
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True, related_name='player_2_record')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.team_name

class Match(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE, blank=True, null=True)
    scheduled_start_time = models.DateTimeField()
    actual_start_time = models.DateTimeField(blank=True, null=True)
    actual_end_time = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE, blank=True, null=True)
    r2_id = models.CharField("R2 ID", max_length=50, blank=True, null=True)
    win_r2_id = models.CharField("R2 Win ID", max_length=50, blank=True, null=True)
    loss_r2_id = models.CharField("R2 Loss ID", max_length=50, blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)