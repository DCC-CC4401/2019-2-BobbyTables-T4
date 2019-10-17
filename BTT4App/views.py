from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from BTT4App.forms import LoginForm, RegisterForm


def landingPage(request):
    return render(request, 'landingPage.html')

def profile(request):
    return render(request, 'userProfile.html')

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.changed_data['username']
            password = form.changed_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request,user)
                return redirect('home/')

    return render(request, 'login.html', {'form': form})

def register(request):
    regForm = RegisterForm()
    if request.method == "POST":
        regForm = RegisterForm(data=request.POST)
        if regForm.is_valid():
            user = regForm.save()
            if user is not None:
                do_login(request,user)
                return redirect('/')
    regForm.fields['name'].help_text = None
    regForm.fields['lastname'].help_text = None
    regForm.fields['email'].help_text = None
    regForm.fields['password'].help_text = None
    regForm.fields['password2'].help_text = None
    return render(request, 'login.html', {'form':regForm})
