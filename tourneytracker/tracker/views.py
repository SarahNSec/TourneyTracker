from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Match, Status, Player, Team
from .forms import StartMatchForm, EndMatchForm
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
    data_dict = {
        'match': match,
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
            match.status = get_object_or_404(Status, status_name="Complete")
            match.actual_end_time = datetime.now()
            match.save()

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
    upcoming_match_list = Match.objects.filter(team__in=players_teams, status__status_name="Not Started").order_by("scheduled_start_time")[:3]
    inprogress_match_list = Match.objects.filter(team__in=players_teams, status__status_name="In Progress").order_by("actual_start_time")
    completed_match_list = Match.objects.filter(team__in=players_teams, status__status_name="Complete").order_by("actual_end_time")[:3]
    data_dict = {
        'player': player,
        'upcoming_match_list': upcoming_match_list,
        'inprogress_match_list': inprogress_match_list,
        'completed_match_list': completed_match_list,
    }
    return render(request, "tracker/player.html", data_dict)