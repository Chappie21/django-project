from django.urls import path
from .api.views import login, check_token

urlpatterns = [
    path('login/', login),
    path('check_token/', check_token)
]