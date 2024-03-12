from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Match, Status
from .forms import StartMatchForm

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