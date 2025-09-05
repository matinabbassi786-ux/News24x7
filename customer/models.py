from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class UserOTP(models.Model):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)

class UserInfo(models.Model):
    Ganderschoices =(
        ("Male","Male"),
        ("Other","Other"),
        ("Female","Female"),
    )
    UserName = models.OneToOneField(User , on_delete=models.CASCADE)
    Ganders = models.CharField(choices=Ganderschoices,max_length=15)
    address = models.CharField(max_length=150 ,blank=True,null=True)
    picture = models.ImageField(upload_to="picture/",blank=True,null=True)