from django.urls import path, include
from .views import *

urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('home/', landingPage, name='landingPage'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]