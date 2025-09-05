from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 
from .models import UserInfo


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'