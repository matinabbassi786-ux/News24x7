from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm,UserInfoForm
from .models import UserOTP
from django.contrib.auth import authenticate, login,logout
from .utils import generate_otp, verify_otp
from django.contrib.auth.models import User,Group
from django.core.mail import send_mail
from django.conf import settings
from .models import UserInfo
from geopy.geocoders import Nominatim
from home.chicking import chickingvalue

def userp(request):
    if chickingvalue(request) == True: return redirect('/')
    return redirect("registration")
    

def RegistrationUser(request):
    if chickingvalue(request) == True: return redirect('/')
    userinfoform = UserInfo()
    userform = RegisterForm()

    date ={
        "userform":userform,
        "userinfoform":userinfoform,
        "usererros":'',
        


    }
    if request.method == 'POST':
        geolocator = Nominatim(user_agent="my_geocoder_app")
        userform = RegisterForm(request.POST)
        ganders = request.POST.get("Ganders")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        location = geolocator.reverse((latitude, longitude))
        if userform.is_valid():
            users = userform.save(commit=False)
            users.username = users.username.lower()
            users.save()
            login(request, users)
            try:
                userinfoform = UserInfo(UserName=request.user,Ganders=ganders,address=location.address)
            except:
                userinfoform = UserInfo(UserName=request.user,Ganders=ganders,address="")
            userinfoform.save()
            try:
                userq1 = User.objects.get(username=request.user)
                groupq2 = Group.objects.get(name='Staff')
                userq1.groups.add(groupq2)
                userq1.save()
            except: 
                    pass           
            try:
                otpq= generate_otp()
                address = request.user.email
                subject = "otp"
                message = str(otpq)
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                otps =UserOTP(email=request.user.email,email_otp=otpq)
                otps.save()
                f = f'/user/verify_otp/{request.user.id}/'
                return redirect(f)
            except:
                a = User(id=request.user.id)
                a.delete()
                erro = "this email already exists"
        else:
            date['usererros'] = str(userform.errors)

    return render(request ,'page/register.html',date)



def verify_otps(request,id):
    if chickingvalue(request) == True: return redirect('/')
    user = UserOTP.objects.get(email=request.user.email)
    if request.method == 'POST':
        email_otp = request.POST['email_otp']
        if email_otp == user.email_otp:
            user.is_email_verified = True
            user.email_otp = None
            user.save()
            return redirect("/")

    date={}
    return render(request ,'page/verify_otp.html',date)

def LoginUser(request):
    if chickingvalue(request) == True: return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            otps = generate_otp()
            user = UserOTP.objects.get(email=request.user.email)
            user.is_email_verified = False
            user.email_otp = otps
            user.save()
            address = request.user.email
            subject = "otp"
            message = str(otps)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
            f = f'/user/verify_otp/{request.user.id}/'
            return redirect(f)
 
    return render(request ,'page/login.html')

def LogOut(request):
     logout(request)
     return redirect("/")

def DeletUser(request):
    return HttpResponse("Delet User")