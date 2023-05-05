from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model

User=get_user_model()
class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15)
    otp=models.CharField(max_length=6)