from django import forms
from django.contrib.auth.models import User,Group
from home.models import News,multipleNewsImageAndVideo,Topic
from .models import StaffMember
from customer.models import UserInfo
class multipleNewsImageAndVideodbform(forms.ModelForm):
    class Meta:
        model = multipleNewsImageAndVideo
        fields = ['image','video']
class NewsImagedb(forms.ModelForm):
    class Meta:
        model = News
        fields = ['Image', 'Video']
      


class StaffMemberdb(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = '__all__'

class Usercreated(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'