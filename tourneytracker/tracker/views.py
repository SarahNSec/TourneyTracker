from django.shortcuts import render
from .models import Match

# Create your views here.
def index(request):
    upcoming_match_list = Match.objects.filter(status__status_name="Not Started").order_by("scheduled_start_time")
    inprogress_match_list = Match.objects.filter(status__status_name="In Progress").order_by("actual_start_time")
    data_dict = {
            'upcoming_match_list': upcoming_match_list,
            'inprogress_match_list': inprogress_match_list,
        }    
    return render(request, "tracker/index.html", data_dict)