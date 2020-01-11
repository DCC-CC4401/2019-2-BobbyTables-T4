from django import forms
from django.contrib.auth.models import User

from BTT4App.models import PersonaNatural


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    image = forms.ImageField(required=False)

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = PersonaNatural
        fields = ['fotoDePerfil']