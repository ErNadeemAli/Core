from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page,),
    path('login',login,name='login'),
    path('register',register,name='register'),
    path('otp',Otp,name='opt'),
]
