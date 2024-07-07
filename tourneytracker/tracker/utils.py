from .models import Player, Tournament
import csv
import pandas as pd

def load_tourney_data(file, tourney_name):
    # First, make sure the tournament is created
    tourney_obj, created = Tournament.objects.get_or_create(
        tourney_name=tourney_name,
        active=True,
    )

    # once the tourney is created, add each of the matches, including 
    # their corresponding objects in other models using the helper functions below.
    df_file = pd.read_csv(file)
    for index, row in df_file.iterrows():
        print(row)
    return None