from django import forms
from .models import Profile


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'height', 'weight', 'gender', 'allergy', 'body_fat', 'current_goal']


class ProfileForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = '__all__'

#
# class ProfileInfoForm(forms.ModelForm):
#     age = models.IntegerField()
#     height = models.DecimalField(max_digits=5, decimal_places=2)
#     weight = models.DecimalField(max_digits=5, decimal_places=2)
#     gender = models.CharField(max_length=20, choices=[('male', 'Male'), ('female', 'Female'),
#                                                       ('prefer_not_to_say', 'Prefer not to say')])
#     allergy = models.CharField(max_length=100, blank=True)
#     body_fat = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
#     current_goal = models.CharField(max_length=20,
#                                     choices=[('lose_weight', 'Lose Weight'), ('maintain_weight', 'Maintain Weight'),
#                                              ('build_muscle', 'Build Muscle')])
