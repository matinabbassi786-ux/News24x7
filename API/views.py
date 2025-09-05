from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import serializers
from home.models import Topic,News,Report,newsLike,FollowingNewsTopic,Comments,multipleNewsImageAndVideo,TrendingTopic,bookmarks,followingStaff
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User,Group
from customer.models import UserInfo,UserOTP
from staff.models import Office,StaffMember,messengStaff


class messengStaffserializers(serializers.ModelSerializer):
    class Meta:
        model = messengStaff
        fields = '__all__'


class StaffMemberserializers(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = '__all__'

class Officeserializers(serializers.ModelSerializer):
      class Meta:
        model = Office
        fields = '__all__'


class UserOTPserializers(serializers.ModelSerializer):
    class Meta:
        model = UserOTP
        fields = '__all__'

class UserInfoserializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class Groupserializers(serializers.ModelSerializer):
     class Meta:
        model = Group
        fields = '__all__' 

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class TrendingTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendingTopic
        fields = '__all__' 
        
        
        
        
class bookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookmarks
        fields = '__all__' 
        
        
class followingStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = followingStaff
        fields = '__all__' 
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__' 
        
        
        
        
class Newsserializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__' 
        

class Reportserializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class newsLikeserializers(serializers.ModelSerializer):
    class Meta:
        model = newsLike
        fields = '__all__'
        

class FollowingNewsTopicserializers(serializers.ModelSerializer):
     class Meta:
        model = FollowingNewsTopic
        fields = '__all__'

class multipleNewsImageAndVideoserializers(serializers.ModelSerializer):
    class Meta:
        model = multipleNewsImageAndVideo
        fields = '__all__'
    
class Commentsserializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
    

# ==================
class topicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class newsviews(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = Newsserializers
    
    
class Reportviews(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = Reportserializers
    
class newsLikeviews(viewsets.ModelViewSet):
    queryset = newsLike.objects.all()
    serializer_class = newsLikeserializers
    
class FollowingNewsTopicviews(viewsets.ModelViewSet):
    queryset = FollowingNewsTopic.objects.all()
    serializer_class = FollowingNewsTopicserializers
    
    
class Commentsviews(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = Commentsserializers
    
class multipleNewsImageAndVideoviews(viewsets.ModelViewSet):
    queryset = multipleNewsImageAndVideo.objects.all()
    serializer_class = multipleNewsImageAndVideoserializers
    
class TrendingTopicviews(viewsets.ModelViewSet):
    queryset = TrendingTopic.objects.all()
    serializer_class = TrendingTopicSerializer

class bookmarksviews(viewsets.ModelViewSet):
    queryset = bookmarks.objects.all()
    serializer_class = bookmarksSerializer
    
class followingStaffview(viewsets.ModelViewSet):
    queryset = followingStaff.objects.all()
    serializer_class = followingStaffSerializer
    
class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers
    
class Groupviews(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Groupserializers
    
class UserInfoviews(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoserializers


class UserOTPviews(viewsets.ModelViewSet):
    queryset = UserOTP.objects.all()
    serializer_class = UserOTPserializers

class Officeviews(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = Officeserializers


class StaffMemberviews(viewsets.ModelViewSet):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberserializers


class messengStaffviews(viewsets.ModelViewSet):
    queryset = messengStaff.objects.all()
    serializer_class = messengStaffserializers