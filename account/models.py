from django.db import models
from django.contrib.auth.models import AbstractUser # we create add aditional informantion base models 
# Create your models here.
from .manager import UserManager


class CustomUser(AbstractUser):
    username=None # we not use username and we user phone number
    phone_number=models.CharField(max_length=20,unique=True)
    email=models.EmailField(unique=True, default='')
    user_bio=models.CharField(max_length=100)
    user_profile_img=models.ImageField(upload_to='profile')
    
    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager()
