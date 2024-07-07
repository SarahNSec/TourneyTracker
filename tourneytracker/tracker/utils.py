from .models import Player, Tournament

def load_tourney_data(file, tourney_name):
    # First, make sure the tournament is created
    tourney_obj, created = Tournament.objects.get_or_create(
        tourney_name=tourney_name,
        active=True,
    )
    if created is False:
        return False

    # once the tourney is created, add each of the matches, including 
    # their corresponding objects in other models using the helper functions below.
    for raw_match in file:
        print(raw_match)
    return None