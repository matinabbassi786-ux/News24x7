from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.index,name='panelstaff'),
   path('data/list/', views.datalist),
   path('editnews/<slug>/<id>/', views.editnews),
   path('multipleim/<id>/<news>',views.multipleimedit),
   path('ckeditor/', include('ckeditor_uploader.urls')),
   path('creatdbtbale/', views.creatdbtbale , name='creatdbtbale' ),
   path('Newsdbcreats/', views.Newsdbcreats , name='Newsdbcreats' ),
   path('topicecreatdb/', views.topicecreatdb , name='topicecreatdb' ),
   path('tinymce/', include('tinymce.urls')),
   path('newsvewsqws/<id>/<slug>', views.newsvewsq ),
   path('Writersrandom/<id>', views.Writersrandom ),
   path('Writerssomeone/<id>', views.Writerssomeone ),
   path('somewriter/<id>/<name>/<id2>', views.somewriter ),
   path('editorsrandom/<id>', views.editorsrandom ),
   path('editorsomeone/<id>', views.editorsomeone ),
   path('uservews/<name>/<id>', views.uservews ),

   path('editorsome/<id>/<name>/<id2>', views.editorsome ),
   path('Statistics', views.Statistics,name='Statistics' ),
   path('Statisticsceo/', views.Statisticsceo , name='Statisticsceo' ),
   path('History/', views.History , name='History' ),
   path('Messages/', views.Messages , name='Messages' ),
   path('StaffAll/', views.StaffAll , name='StaffAll' ),
   path('Staffadd/', views.Staffadd , name='Staffadd' ),
   path("creatStaff/", views.Staffcreate , name="Staffcreate" ),
   path("creatStaff/<pk>", views.Staffcreate2 , name="Staffcreate2" )
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)