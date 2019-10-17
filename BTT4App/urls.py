from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('index/', landingPage, name='landingPage'),
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('accounts/', include('django.contrib.auth.urls'))
]