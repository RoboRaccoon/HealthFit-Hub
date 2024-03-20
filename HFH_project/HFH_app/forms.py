from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['photo', 'name', 'email', 'age', 'height', 'weight', 'gender', 'allergy', 'body_fat', 'current_goal']
