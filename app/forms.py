from django import forms
from app.models import Profile

class ProfileForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email')

    class Meta:
        model=Profile
        fields=['name','email']