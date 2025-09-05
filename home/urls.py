from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('' , views.index, name='home'),
   path('profile/' , views.profile, name='profile'),
   path('<slug>' , views.newsviews, name='newsviews'),
   path('Topic/<NewsTopic>/' , views.topicviews, name='topicfllows'),
   path('like/<id>' , views.newslike, name='like'),
   path('bookmarks/<id>' , views.bookmarksuser, name='bookmarks'),
   path('unbookmarks/<id>' , views.unbookmarksuser, name='unbookmarksuser'),
   path('followingnewstopic/<Topics>/<id>' , views.followingnewstopicuser, name='followingnewstopic'),
   path('unfollowingnewstopic/<Topics>/<id>' , views.unfollowingnewstopicuser, name='followingnewstopic'),
   path('followingftaffuser/<staffmembername>/<id>' , views.followingStaffUser, name='followingftaffuser'),
   path('unfollowingftaffuser/<staffmembername>/<id>' , views.unfollowingStaffUser, name='unfollowingftaffuser'),
   path('comment/<comment>/<id>', views.commentonnews),
   path('report/<id>', views.reportnews),
   path('commentall/<id>', views.commentsseeaall),
   path('staff/<name>/<id>', views.staffviews),
   path('followingftaffuser2/<name>/<id>', views.followingStaffUser2),
   path('unfollowingnewstopic2/<name>/<id>', views.unfollowingStaffUser2),
   path("topicfollowing/",views.allfollowinglisttopic),
   path("unfollowingnewstopic3/<topic>/<id>", views.unfollowingnewstopicuser20 ),
   path("followingnewstopic3/<topic>/<id>", views.followingnewstopicuser20 ),
   path("followingall/", views.followingall),
   path('bookmark/' , views.bookmarklist ),
   path('Hindi/<id>/<title>', views.Hindi ),
   path('Gujarati/<id>/<title>', views.Gujarati ),
   path("aboutus/", views.about_us , name="aboutus"),
   path("ContactUs/", views.ContactUs , name="ContactUs"),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)