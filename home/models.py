from django.db import models
from staff.models import StaffMember
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from staff.models import StaffMember


class Topic(models.Model):
    Topic = models.CharField(max_length=20,unique=True)
    Date = models.DateField(auto_now_add=True)
    CreatedBy = models.ForeignKey(StaffMember,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.Topic

class News(models.Model):
    Topic = models.ForeignKey(Topic ,on_delete=models.CASCADE,blank=True,null=True)
    Journalists = models.ForeignKey(StaffMember,related_name="Journalists",on_delete=models.CASCADE,default="sorry",blank=True,null=True)
    Writers = models.ForeignKey(StaffMember,related_name="Writers",on_delete=models.CASCADE,default="sorry" ,blank=True,null=True)
    Editors = models.ForeignKey(StaffMember,related_name="Editors",on_delete=models.CASCADE,default="sorry",blank=True,null=True)
    NewsTitle = models.CharField(max_length=250,blank=True,null=True)
    Txt =   HTMLField(blank=True,null=True)
    Image = models.ImageField(upload_to="image/",blank=True,null=True)
    Video = models.FileField(upload_to="video/",blank=True,null=True)
    CreatDate = models.DateField(auto_now_add=True)
    onlyvideo = models.BooleanField(default=False)
    JournalistsPermission = models.BooleanField(blank=True,null=True)
    WritersPermission = models.BooleanField(blank=True,null=True )
    EditorsPermission = models.BooleanField(blank=True,null=True )
    ManagersPermission = models.BooleanField(blank=True,null=True )
    slug = AutoSlugField(populate_from='NewsTitle')
    # Collaboration = models.ManyToManyField(StaffMember,blank=True)
    def __str__(self):
        return self.NewsTitle
    

class Report(models.Model):
    News = models.ForeignKey(News,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=75)
    Txt = models.TextField(max_length=500)
    slug = AutoSlugField(populate_from='Txt')

class newsLike(models.Model):
    News = models.OneToOneField(News ,on_delete=models.CASCADE)
    User = models.ManyToManyField(User,blank=True)

class FollowingNewsTopic(models.Model):
    NewsTopic = models.OneToOneField(Topic,on_delete=models.CASCADE)
    User = models.ManyToManyField(User,blank=True)

class Comments(models.Model):
    UserName = models.ForeignKey(User,on_delete=models.CASCADE)
    news = models.ForeignKey(News , on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='text')

class multipleNewsImageAndVideo(models.Model):
    news = models.ForeignKey(News , on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/", blank=True ,null=True)
    video = models.FileField(upload_to="video/" , blank=True ,null=True)

class TrendingTopic(models.Model):
    NewsTopic = models.OneToOneField(Topic,on_delete=models.CASCADE) 
    Date = models.DateTimeField(auto_now_add=True)


# class ReplyByNews24x7(models.Model):
#     to = models.ForeignKey(User,on_delete=models.CASCADE)
#     txt = HTMLField()
#     date = models.DateField(auto_now_add=True)
#     slug = AutoSlugField(populate_from='txt')

# class Countus(models.Model):
#     user = models.ForeignKey(User ,on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     txt = models.TextField(max_length=500)
#     slug = AutoSlugField(populate_from='title')

# class NewsBlogPage(models.Model):
#     title = models.CharField(max_length=50)
#     image = models.ImageField(upload_to="image/")
#     txt = HTMLField()
#     date = models.DateField(auto_now_add=True)
#     slug = AutoSlugField(populate_from='title')


class bookmarks(models.Model):
    News = models.OneToOneField(News,on_delete=models.CASCADE)
    User = models.ManyToManyField(User,blank=True,default="")

class followingStaff(models.Model):
    StaffMemberName = models.OneToOneField(StaffMember,on_delete=models.CASCADE)
    User = models.ManyToManyField(User,blank=True,default="")