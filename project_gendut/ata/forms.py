from django import forms
from .models import Mentor

class Input_Mentor(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('id', 'name', 'position','experience','comment','photo')