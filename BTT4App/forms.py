from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    name = forms.CharField()
    lastName = forms.CharField()
    mail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPass = forms.CharField(widget=forms.PasswordInput())