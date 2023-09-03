from django.urls import path
from . import views

urlpatterns = [
    path("login" , views.user_login),
    path("logout" , views.user_logout),
    path("register" , views.user_register),
]