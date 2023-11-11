from django.urls import path
from .api.views import login, check_token, register

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('check_token/', check_token)
]