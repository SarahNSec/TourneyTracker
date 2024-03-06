from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path('', views.index, name="index"),
    path('match/<int:pk>', views.match, name="match"),
]
