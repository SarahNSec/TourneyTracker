from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Match, Location, Court

class StartMatchForm(forms.ModelForm):
    class Meta:
         model = Match
         fields = ["court"]
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['court'].queryset = Court.objects.filter(location=self.instance.location)

class EndMatchForm(forms.ModelForm):
    class Meta:
         model = Match
         fields = ["outcome"]

class LoadTourneyDataForm(forms.Form):
    tournament_name = forms.CharField(max_length=50)
    file = forms.FileField()