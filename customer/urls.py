from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.userp),
    path('registration/', views.RegistrationUser, name="registration"),
    path('verify_otp/<id>/', views.verify_otps, name='verify_otp'),
    path('login/',views.LoginUser, name="login"),
    path('logout/', views.LogOut, name="logout"),
    path('deletuser/', views.DeletUser, name="deletuser"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
