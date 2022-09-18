from django import forms

class LeagueForm(forms.Form):
    league_id = forms.IntegerField(label='Please enter league id')