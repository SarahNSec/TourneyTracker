from .models import Tournament, Team, Location, Match, Division, Status
from datetime import datetime
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
    for index, match in df_file.iterrows():
        # Get the match details
        team_obj = Team.objects.get(team_name=match['team'])
        location_obj = Location.objects.get(abbreviation=match['location'])
        start_time = datetime.strptime(match['scheduled_start_time'], '%m/%d/%y %H:%M')
        status = Status.objects.get(status_name=match['status'])
        r2_id = match['r2_id']
        win_r2_id = match['win_r2_id']
        loss_r2_id = match['loss_r2_id']
        division, div_created = Division.objects.get_or_create(div_name=match['division'], tournament=tourney_obj)

        # create the match record
        match_obj = Match(
            team=team_obj,
            location=location_obj,
            scheduled_start_time=start_time,
            status=status,
            r2_id=r2_id,
            win_r2_id=win_r2_id,
            loss_r2_id=loss_r2_id,
            division=division
        )
        match_obj.save()
        
    return None