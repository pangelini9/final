from django import forms
from .models import Attempt

class AttemptForm(forms.ModelForm):
    class Meta:
        model = Attempt
        fields = ['quiz choice']
        labels = {'quiz choice': 'which_quiz'}






