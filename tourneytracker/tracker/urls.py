from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path('', views.index, name="index"),
    path('match/<int:pk>', views.match, name="match"),
    path('match/<int:pk>/start', views.start_match, name="start_match"),
    path('match/<int:pk>/end', views.end_match, name="end_match"),
    path('player/<int:pk>', views.player, name="player"),   
]
