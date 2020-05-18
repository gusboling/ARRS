from django import forms
from core.models import Comp, Tournament

class CompForm(forms.Form):
    name = forms.CharField(label="Competitor/Team Name ", max_length=100)

class TournamentForm(forms.Form):
    name = forms.CharField(label="Tournament Name ", max_length=100)
    location = forms.CharField(label="Location", max_length=100)
    date = forms.DateField(label="Date (yyyy-mm-dd)", widget=forms.SelectDateWidget)

class RoundForm(forms.Form):
    #TODO: Make this an auto-complete select
    debater = forms.ModelChoiceField(queryset=Comp.objects.all())
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())

    ROUND_TYPES = [
        ("PRE", "Preliminary"),
        ("OCT", "Octafinal"),
        ("QRT", "Quarterfinal"),
        ("SEM", "Semifinal"),
        ("FIN", "Final"),
        ("OTH", "Other")
    ]

    EVENT_TYPES = [
        ("VPO", "Varsity Policy"),
        ("VLD", "Varsity Lincoln-Douglas"),
        ("VPF", "Public Forum"),
        ("NPO", "Novice Policy"),
        ("NLD", "Novice Lincoln-Douglas"),
        ("OTH", "Other")
    ]

    opponent = forms.CharField(label="Opponent Name", max_length=100)
    bracket = forms.ChoiceField(label="Round Type", widget=forms.Select, choices=ROUND_TYPES)
    event = forms.ChoiceField(label="Event", widget=forms.Select, choices=EVENT_TYPES)
    won = forms.BooleanField(label="Round Won")
    position = forms.BooleanField(label="Round Position")
    
