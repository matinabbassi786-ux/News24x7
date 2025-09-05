from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include("home.urls"),name="index"),
    path('user/', include("customer.urls") ,name="registration"),
     path('tinymce/', include('tinymce.urls')),
      path('ckeditor/', include('ckeditor_uploader.urls')),
     path('panelstaff/', include('staff.urls')),
     path('api/', include("API.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)