from django import forms

class CompForm(forms.Form):
    name = forms.CharField(label="Competitor/Team Name ", max_length=100)

class TournamentForm(forms.Form):
    name = forms.CharField(label="Tournament Name ", max_length=100)
    location = forms.CharField(label="Location", max_length=100)
    date = forms.DateField(label="Date (yyyy-mm-dd)", widget=forms.SelectDateWidget)

class Round(forms.Form):
    #TODO: Make this a dropdown/search
    #debater = forms.CharField(label="Competitor")
    pass
