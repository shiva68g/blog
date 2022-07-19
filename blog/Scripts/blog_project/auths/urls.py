import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('register' , registeruser ),
    path('login' , loginuser),
    path('logout' , userlogout)
]
