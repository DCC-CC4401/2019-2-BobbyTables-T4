from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')

def profile(request):
    return render(request, 'userProfile.html')

def login(request):
    return render(request, 'login.html')
