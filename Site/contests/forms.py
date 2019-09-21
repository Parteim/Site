from django import forms
from .models import Participants


class ParticipantForm(forms.Form):
    contest = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'contest__name',
        'type': 'hidden',
    }))

    fields = ['contest']
