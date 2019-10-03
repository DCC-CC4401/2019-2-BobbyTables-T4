from django.urls import path
from .views import *

urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('profile/', profile, name='profile'),
]