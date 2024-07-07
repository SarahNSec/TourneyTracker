from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Match, Status, Player, Team, Division
from .forms import StartMatchForm, EndMatchForm, LoadTourneyDataForm
from django.db.models import Q

# Create your views here.
def index(request):
    upcoming_match_list = Match.objects.filter(status__status_name="Not Started").order_by("scheduled_start_time")
    inprogress_match_list = Match.objects.filter(status__status_name="In Progress").order_by("actual_start_time")
    data_dict = {
            'upcoming_match_list': upcoming_match_list,
            'inprogress_match_list': inprogress_match_list,
        }    
    return render(request, "tracker/index.html", data_dict)

def match(request, pk):
    match = Match.objects.get(pk=pk)
    win_match_list = []
    loss_match_list = []
    if match.win_r2_id is not None:
        win_match_list.append(Match.objects.get(r2_id=match.win_r2_id))
    if match.loss_r2_id is not None:
        loss_match_list.append(Match.objects.get(r2_id=match.loss_r2_id))
    data_dict = {
        'main_match_list': [match],
        'win_match_list': win_match_list,
        'loss_match_list': loss_match_list,
    }
    return render(request, "tracker/match.html", data_dict)

def start_match(request, pk):
    match = get_object_or_404(Match, pk=pk)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StartMatchForm(request.POST, instance=match)
        # check whether it's valid:
        if form.is_valid():
            # TODO: add validation that a valid court was chosen.  If "----" was chosen, need to reset everything
            # The form is bound, so the court is already updated, but I still need to update 
            # the status and start time
            match.status = get_object_or_404(Status, status_name="In Progress")
            match.actual_start_time = datetime.now()
            match.save()

            # redirect to a new URL:
            return render(request, "tracker/match.html", {'match': match})
    else:
        # check that match is in status "Not Started" since only 
        # "Not Started" matches can be started
        if match.status.status_name != "Not Started":
            # If this is the case, just reload the page
            return render(request, "tracker/match.html", {'match': match})
        else:
            # The match is in the right status, so load the "start match" page
            match_form = StartMatchForm(instance=match)
            return render(request, "tracker/start_match.html", {'match_form': match_form, 'match': match})
        
def end_match(request, pk):
    match = get_object_or_404(Match, pk=pk)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EndMatchForm(request.POST, instance=match)
        # check whether it's valid:
        if form.is_valid():
            # if valid, first we update the current match
            match.status = get_object_or_404(Status, status_name="Complete")
            match.actual_end_time = datetime.now()
            match.save()

            # Next we update future matches based on the outcome to mark matches 
            # that won't be played "Not Applicable".  
            if match.outcome.outcome_name == 'Win':
                # When the match was won, we want to iteratively mark the loss trail as not applicable
                pass
            elif match.outcome.outcome_name == 'Loss':
                # When the match was lost, we want to iteratively mark the win trail as not applicable
                pass

            # redirect to a new URL:
            return render(request, "tracker/match.html", {'match': match})
    else:
        # check that match is in status "In Progress" since only 
        # "In Progress" matches can be ended
        if match.status.status_name != "In Progress":
            # If this is the case, just reload the page
            return render(request, "tracker/match.html", {'match': match})
        else:
            # The match is in the right status, so load the "end match" page
            match_form = EndMatchForm(instance=match)
            return render(request, "tracker/end_match.html", {'match_form': match_form, 'match': match})

def player(request, pk):
    player = Player.objects.get(pk=pk)
    players_teams = Team.objects.filter(Q(player_1=pk) | Q(player_2=pk))
    divisions = Division.objects.filter(team__in=players_teams)
    upcoming_match_list = Match.objects.filter(team__in=players_teams, status__status_name="Not Started").order_by("scheduled_start_time")[:3]
    inprogress_match_list = Match.objects.filter(team__in=players_teams, status__status_name="In Progress").order_by("actual_start_time")
    completed_match_list = Match.objects.filter(team__in=players_teams, status__status_name="Complete").order_by("actual_end_time")[:3]
    data_dict = {
        'player': player,
        'divisions': divisions,
        'upcoming_match_list': upcoming_match_list,
        'inprogress_match_list': inprogress_match_list,
        'completed_match_list': completed_match_list,
    }
    return render(request, "tracker/player.html", data_dict)

def players(request):
    """
    Displays a page that shows all players
    """
    players = Player.objects.all().order_by("player_name")
    data_dict = {
        'players': players,
    }
    return render(request, "tracker/players.html", data_dict)

def load_tourney(request):
    """
    Allows loading tournament data in a csv format
    """
    if request.method == 'POST':
        form = LoadTourneyDataForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["file"])
            return redirect('tracker:index')
    else:
        # method == 'GET' -> loading page initially
        form = LoadTourneyDataForm()
        return render(request, "tracker/load_tourney.html", {'form': form})
        