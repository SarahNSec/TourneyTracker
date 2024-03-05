from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=256)

    def __str__(self):
        return self.player_name

class Tournament(models.Model):
    tourney_name = models.CharField("Tournament Name", max_length=256)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.tourney_name