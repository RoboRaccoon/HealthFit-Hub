from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    height = forms.DecimalField(label='Height (cm)', max_digits=5, decimal_places=2)
    weight = forms.DecimalField(label='Weight (kg)', max_digits=5, decimal_places=2)
    email = forms.EmailField(label='Email')
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    photo = forms.ImageField(label='Profile Photo', required=False)
