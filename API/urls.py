from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'User', views.UserViews)
router.register(r'Group', views.Groupviews)
router.register(r'User Info', views.UserInfoviews)
router.register(r'User OTP', views.UserOTPviews)
router.register(r'Topic', views.topicViewSet)
router.register(r'News', views.newsviews)
router.register(r'Report', views.Reportviews)
router.register(r'News Like', views.newsLikeviews)
router.register(r'Following News', views.FollowingNewsTopicviews)
router.register(r'Comments', views.Commentsviews)
router.register(r'Multiple News Image And Video', views.multipleNewsImageAndVideoviews)
router.register(r'Trending Topic', views.TrendingTopicviews)
router.register(r'Bookmarks', views.bookmarksviews)
router.register(r'following Staff', views.followingStaffview)
router.register(r'Office', views.Officeviews)
router.register(r'Staff Member', views.StaffMemberviews)
router.register(r'messeng Staff', views.messengStaffviews)


urlpatterns = [
    path('', include(router.urls)),
]