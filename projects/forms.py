from django import forms
from .models import Profile,Projects

class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude = ['projects']

class NewProjectsForm(forms.ModelForm):
    class Meta:
        model=Projects
        exclude= []