from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from BTT4App.models import *

# Create your views here.
from BTT4App.forms import LoginForm, RegisterForm

@login_required(login_url='../login/')
def landingPage(request):
    return render(request, 'landingPage.html')

@login_required(login_url='../login/')
def profile(request):
    return render(request, 'userProfile.html')


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request,user)
                #return render(request, 'landingPage.html')
                return HttpResponseRedirect(request.GET['next'])
        regForm = RegisterForm(data=request.POST)
        print(regForm.errors)
        if regForm.is_valid():
            if User.objects.filter(username=regForm.cleaned_data['email']).exists():
                return render(request, 'login.html', {'form': form,
                                                      'error_massage': 'Email existente, utilice otro'})
            elif regForm.cleaned_data['password'] != regForm.cleaned_data['password2']:
                return  render(request, 'login.html', {'form': form,
                                                       'error_message':'Contraseñas no coinciden'})
            else:
                user = PersonaNatural()
                user.create_persona(regForm.cleaned_data['name'],
                                    regForm.cleaned_data['lastname'],
                                    regForm.cleaned_data['email'],
                                    regForm.cleaned_data['password'])

                user = authenticate(username=regForm.cleaned_data['email'], password=regForm.cleaned_data['password'])
                if user is not None:
                    do_login(request,user)
                    #return render(request, 'landingPage.html')
                    return HttpResponseRedirect(request.GET['next'])
    return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == "GET":
        do_logout(request)
        return redirect('/')

