from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from BTT4App.models import *

# Create your views here.
from BTT4App.forms import LoginForm, RegisterForm, ProfilePictureForm, ChangePassForm


@login_required(login_url='../login/')
def landingPage(request):
    return render(request, 'landingPage.html')


@login_required(login_url='../login/')
def profile(request):
    if request.method == 'POST':

        pass_form = ChangePassForm(data=request.POST)
        if pass_form.is_valid():
            oldpassword = pass_form.cleaned_data['oldpassword']
            newpassword = pass_form.cleaned_data['newpassword']
            newpassword2 = pass_form.cleaned_data['newpassword2']
            user = request.user
            if user.check_password(oldpassword) and newpassword == newpassword2:
                user.set_password(newpassword)
                user.save()
                messages.success(request, f'Tu contraseña ha sido actualizada')
                log_user = authenticate(username=user.username, password=newpassword)
                if log_user is not None:
                    do_login(request, log_user)
                return redirect('profile')

        p_form = ProfilePictureForm(request.POST,
                                    request.FILES,
                                    instance=request.user.personanatural
                                    )
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Tu cuenta ha sido actualizada')
            return redirect('profile')

    else:

        p_form = ProfilePictureForm(instance=request.user.personanatural)

    context = {
        'p_form': p_form
    }

    return render(request, 'userProfile.html', context)


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                # return render(request, 'landingPage.html')
                return HttpResponseRedirect(request.GET['next'])
        u_form = RegisterForm(data=request.POST, files=request.FILES)
        print(u_form.errors)
        if u_form.is_valid():

            if User.objects.filter(username=u_form.cleaned_data['email']).exists():
                return render(request, 'login.html', {'form': form,
                                                      'error_massage': 'Email existente, utilice otro'})
            elif u_form.cleaned_data['password'] != u_form.cleaned_data['password2']:
                return render(request, 'login.html', {'form': form,
                                                      'error_message': 'Contraseñas no coinciden'})
            else:
                user = PersonaNatural()

                user.create_persona(u_form.cleaned_data['name'],
                                    u_form.cleaned_data['lastname'],
                                    u_form.cleaned_data['email'],
                                    u_form.cleaned_data['password'],
                                    u_form.cleaned_data['image']
                                    )



                user = authenticate(username=u_form.cleaned_data['email'], password=u_form.cleaned_data['password'])
                if user is not None:
                    do_login(request, user)
                    # return render(request, 'landingPage.html')
                    return HttpResponseRedirect(request.GET['next'])

    return render(request, 'login.html', {'form': form})


def logout(request):
    if request.method == "GET":
        do_logout(request)
        return redirect('/')

