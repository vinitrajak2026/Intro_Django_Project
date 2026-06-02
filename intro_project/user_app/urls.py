from django.urls import path
from .views import greet, getname, users, greet_to_user

urlpatterns = [
    path('message/', greet),
    path('getname/', getname),
    path('users/', users),
    path('greet/<str:name>/', greet_to_user),
]