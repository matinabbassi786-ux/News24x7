from django.contrib import admin
from .models import Topic,News,newsLike,FollowingNewsTopic,Comments,multipleNewsImageAndVideo,TrendingTopic,bookmarks,followingStaff,Report

admin.site.register(Report)
admin.site.register(Topic)
admin.site.register(News) 
admin.site.register(newsLike) 
admin.site.register(FollowingNewsTopic) 
admin.site.register(Comments) 
admin.site.register(multipleNewsImageAndVideo)   
admin.site.register(TrendingTopic)
admin.site.register(bookmarks)   
admin.site.register(followingStaff)   
