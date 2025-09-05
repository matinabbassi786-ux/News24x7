
from django.shortcuts import render,redirect
from .models import News,TrendingTopic,Topic,newsLike,bookmarks,Comments,FollowingNewsTopic,followingStaff,Report,multipleNewsImageAndVideo
from customer.models import UserInfo
from staff.models import StaffMember
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .chicking import chickingvalue
from customer.models import UserInfo,UserOTP
from django import forms
import asyncio
from googletrans import Translator
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
import random
import python_weather
import asyncio
import os

def remove_html_tags_bs4(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    return soup.get_text()





class UserInfoForm(forms.ModelForm):
        class Meta:
            model = UserInfo
            fields = ['picture']
            
            
def index(request):       
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.all().filter(ManagersPermission=True,onlyvideo=False)[::-1]
    newsdb2 = News.objects.all().filter(ManagersPermission=True,onlyvideo=True)[::-1]
    TrendingTopicdb = TrendingTopic.objects.all()[::-1]
    alltopic = Topic.objects.all()[::-1]
    async def main() -> None:
      async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    
        weather = await client.get('Surat, Gujarat')
        return {
        "temperature":weather.temperature,
        "humidity":weather.humidity,
        "feels_like":weather.feels_like,
        "description":weather.description,
        "datetime":weather.datetime,
        }
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
    qrow  = asyncio.run(main())
    date ={
        'newsdb':newsdb,
        'TrendingTopicdb':TrendingTopicdb,
        "alltopic":alltopic,
        "newsdb2":newsdb2,
        "temperature":qrow["temperature"],
        "humidity":qrow["humidity"],
        "feels_like":qrow["feels_like"],
        "description":qrow["description"],
        "datetime":qrow["datetime"],
        
    }
    return render(request ,'page/index.html',date)

def newsviews(request,slug):
        if chickingvalue(request) == False: return redirect('user/login/')
        UserInfodb = UserInfo.objects.all()
        newsdb = News.objects.get(slug=slug)
        allnewsdb = News.objects.all().filter(Journalists=newsdb.Journalists,JournalistsPermission=True,onlyvideo=False)[::-1]
        writers = StaffMember.objects.all().filter(staff_name=newsdb.Writers)
        editors = StaffMember.objects.all().filter(staff_name=newsdb.Editors)
        journalists = StaffMember.objects.all().filter(staff_name=newsdb.Journalists)
    
        multiplimageandvideo = multipleNewsImageAndVideo.objects.all().filter(news=newsdb)
    
        multiplimageandvideocount = multipleNewsImageAndVideo.objects.all().filter(news=newsdb).count()
   
        staffdb = StaffMember.objects.get(staff_name=newsdb.Journalists)
        TrendingTopicdb = TrendingTopic.objects.all()[::-1]
        yas = 0
        no = 0
        yasno =0
        followingnuber = 0
        Commenmaxnu = 0
        try:
            Commenmax = Comments.objects.all().filter(UserName=request.user).count()
            if Commenmax >= 3:
                Commenmaxnu = 1
        except:pass
        try:
            followingStaffcount = followingStaff.objects.get(StaffMemberName=staffdb)
            followingStaffcountss = followingStaffcount.User.all().count()

        except: followingStaffcountss =0
        try:
            followingstaffs = followingStaff.objects.get(StaffMemberName=staffdb)
            for x in followingstaffs.User.all():
                if x == request.user:
                    followingnuber = 1
        except:pass
        try:
            bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=newsdb.Topic)
            for x in bookmarksdb.User.all():
                if x == request.user:
                    yasno = 1
        except:pass
        try:
            Commen = Comments.objects.all().filter(news=newsdb)[::-1]
            Commencount = Comments.objects.all().filter(news=newsdb).count()

        except:
            Commen =0
            Commencount =0
        try:
            newsLikedb = newsLike.objects.get(News=newsdb.id)
            count = newsLikedb.User.all().count()
            for x in newsLikedb.User.all():
                if x == request.user:
                    yas = 1
        except:
            count= 0
            newsLikedb = []
        try:
            bookmarksdb = bookmarks.objects.get(News=newsdb.id)
            for x in bookmarksdb.User.all():
                if x == request.user:
                    no = 1

        except:pass
        if request.method == 'POST':
           comment= request.POST.get("comments")
           return redirect("/comment/"+str(comment)+"/"+str(newsdb.id))
        newsdb2 = News.objects.all().filter(onlyvideo=False,ManagersPermission=True,EditorsPermission=True,WritersPermission=True,JournalistsPermission=True)
        five_unique_elements = random.choices(newsdb2,k=20)
        date ={
            'newsdb':newsdb,
            'staffdb':staffdb,
            'TrendingTopicdb':TrendingTopicdb,
            'count':count,
            'newsLikedb':newsLikedb,
            'yas':yas,
            'no':no,
            'Commen':Commen,
            'UserInfodb':UserInfodb,
            'Commencount':Commencount,
            'yasno':yasno,
            "followingnuber":followingnuber,
            "followingStaffcountss":followingStaffcountss,
            'Commenmaxnu':Commenmaxnu,
            'multiplimageandvideo':multiplimageandvideo,
            "multiplimageandvideocount":multiplimageandvideocount,
            'allnewsdb':allnewsdb,
            'writers':writers,
            'editors':editors,
            'journalists':journalists,
            'five_unique_elements':five_unique_elements
        }
        return render(request ,'page/newsviews.html',date)
    



def topicviews(request,NewsTopic):
    if chickingvalue(request) == False: return redirect('user/login/')
    TrendingTopicdb = TrendingTopic.objects.all()[::-1]
    Topicdb = Topic.objects.get(Topic = NewsTopic)
    newsdb = News.objects.all().filter(Topic=Topicdb.id,onlyvideo=False)[::-1]
    totlenewsdb = News.objects.all().filter(Topic=Topicdb.id).count()
    yasno = 0
    try:
        bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=Topicdb)
        for x in bookmarksdb.User.all():
            if x == request.user:
                yasno = 1
    except:
            pass
    
    date = {
        'Topicdb':Topicdb,
        'newsdb':newsdb,
        'totlenewsdb':totlenewsdb,
        'TrendingTopicdb':TrendingTopicdb,
        'yasno':yasno,
      
    }
    return render(request ,'page/topicniews.html',date)


def profile(request):
    if chickingvalue(request) == False: return redirect('user/login/')
    userinfo = UserInfo.objects.get(UserName=request.user)
    dbform = UserInfoForm(request.POST, request.FILES, instance=userinfo)
    if request.method == 'POST':
        dbform = UserInfoForm(request.POST, request.FILES, instance=userinfo)
        if dbform.is_valid():
            dbform.save()
            return redirect('/')

    data ={
        'dbform':dbform,
        'userinfo':userinfo
    }
    return render(request ,'page/profile.html',data)

def newslike(request,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    try:
        newsLikedb = newsLike.objects.get(News=newsdb.id)
        newsLikedb.User.add(request.user)
        newsLikedb.save()
    except:
        newsLikedb = newsLike.objects.create(News=newsdb)
        newsLikedb.save()
        newsLikedb.User.add(request.user)
        newsLikedb.save()

    count = newsLikedb.User.all().count()
    date ={
        "newsLikedb":newsLikedb,
        'count':count
    }
    urls = "/"+str(newsdb.slug)
    return redirect(urls)


def unbookmarksuser(request,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    try:
        bookmarksdb = bookmarks.objects.get(News=newsdb.id)
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = bookmarks.objects.create(News=newsdb)
        bookmarksdb.save()
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    urls = "/"+str(newsdb.slug)
    return redirect(urls)

def bookmarksuser(request,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    try:
        bookmarksdb = bookmarks.objects.get(News=newsdb.id)
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = bookmarks.objects.create(News=newsdb)
        bookmarksdb.save()
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    urls = "/"+str(newsdb.slug)
    return redirect(urls)

def followingnewstopicuser(request,Topics,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    Topicdb = Topic.objects.get(Topic=Topics)
    newsdb = News.objects.get(id=id)
    try:
        bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=Topicdb.id)
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = FollowingNewsTopic.objects.create(NewsTopic=Topicdb)
        bookmarksdb.save()
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    urls = "/"+str(newsdb.slug)
    return redirect(urls)


def unfollowingnewstopicuser(request,Topics,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    Topicdb = Topic.objects.get(Topic=Topics)
    newsdb = News.objects.get(id=id)
    try:
        bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=Topicdb.id)
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = FollowingNewsTopic.objects.create(NewsTopic=Topicdb)
        bookmarksdb.save()
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    urls = "/"+str(newsdb.slug)
    return redirect(urls)

def followingStaffUser(request,staffmembername,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    staffmember =  StaffMember.objects.get(staff_name=staffmembername)
    try:
        bookmarksdb = followingStaff.objects.get(StaffMemberName=staffmember)
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = followingStaff.objects.create(StaffMemberName=staffmember)
        bookmarksdb.save()
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    urls = "/"+str(newsdb.slug)
    return redirect(urls)

def unfollowingStaffUser(request,staffmembername,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    staffmember =  StaffMember.objects.get(staff_name=staffmembername)
    try:
        bookmarksdb = followingStaff.objects.get(StaffMemberName=staffmember)
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = followingStaff.objects.create(StaffMemberName=staffmember)
        bookmarksdb.save()
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    urls = "/"+str(newsdb.slug)
    return redirect(urls)


def commentonnews(request,comment,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    commentdb = Comments.objects.create(UserName=request.user,news=newsdb,text=comment)
    commentdb.save()
    commentdb.clean()
    return redirect("/"+str(newsdb.slug))


def reportnews(request,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    qua = 0
    try:
        reportsl = Report.objects.get(user=request.user)
        qua = 1
    except:
        reportsl = ''
        qua = 0
    data ={
        'newsdb':newsdb,
        'reportsl':reportsl
    }
    if request.method == 'POST' and qua == 0:
        rreport = request.POST.get("Report")
        rreportsz = request.POST.get("Subject")
        Reports = Report.objects.create(News=newsdb,Title=rreportsz,Txt=rreport,user=request.user)
        Reports.save()
        return redirect("/"+str(newsdb.slug))
    if request.method == 'POST' and qua == 1:
        rreport = request.POST.get("Report")
        rreportsz = request.POST.get("Subject")
        reportsl.title = rreport
        reportsl.Txt = rreportsz
        reportsl.save()
        return redirect("/"+str(newsdb.slug))

    return render(request,'page/report.html',data)



def commentsseeaall(request,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    newsdb = News.objects.get(id=id)
    commentsall = Comments.objects.all().filter(news=newsdb)
    commentsallcount = Comments.objects.all().filter(news=newsdb).count()
    UserInfodb = UserInfo.objects.all()
    TrendingTopicdb = TrendingTopic.objects.all()[::-1]
    data ={
        'newsdb':newsdb,
        'commentsall':commentsall,
        'commentsallcount':commentsallcount,
        'UserInfodb':UserInfodb,
        'TrendingTopicdb':TrendingTopicdb
    }
    return render(request,'page/commentssee.html',data)


def staffviews(request,name,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    StaffMemberdb = StaffMember.objects.get(id=id)
    Newsdb = News.objects.all().filter(Journalists=StaffMemberdb,JournalistsPermission=True,onlyvideo=False)
    totleNewsdb = News.objects.all().filter(Journalists=StaffMemberdb,JournalistsPermission=True).count()
    TrendingTopicdb = TrendingTopic.objects.all()[::-1]
    totlelikes = 0
    followingnuber = 0
    followingStafftotle =0
    try:
        for x in Newsdb:
            qurd = newsLike.objects.all().filter(News=x)
            for y in qurd:
                totlelikes += y.User.all().count()
    except:pass
    try:
        followingstaffs = followingStaff.objects.get(StaffMemberName=StaffMemberdb)
        followingStafftotle = followingStaff.objects.get(StaffMemberName=StaffMemberdb)
        followingStafftotle = followingStafftotle.User.all().count
        for x in followingstaffs.User.all():
            if x == request.user:
                followingnuber = 1
    except:pass
    data ={
        'StaffMemberdb':StaffMemberdb,
        'Newsdb':Newsdb,
        'TrendingTopicdb':TrendingTopicdb,
        'followingnuber':followingnuber,
        'totleNewsdb':totleNewsdb,
        'followingStafftotle':followingStafftotle,
        'totlelikes':totlelikes
    }
    return render(request,'page/staffviews.html',data)


def followingStaffUser2(request,name,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    staffmember =  StaffMember.objects.get(id=id)
    try:
        bookmarksdb = followingStaff.objects.get(StaffMemberName=staffmember)
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = followingStaff.objects.create(StaffMemberName=staffmember)
        bookmarksdb.save()
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    urls = '/staff'+'/'+str(staffmember.staff_name)+'/'+str(staffmember.id)
    return redirect(urls)

def unfollowingStaffUser2(request,name,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    staffmember =  StaffMember.objects.get(id=id)
    try:
        bookmarksdb = followingStaff.objects.get(StaffMemberName=staffmember)
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = followingStaff.objects.create(StaffMemberName=staffmember)
        bookmarksdb.save()
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    urls = '/staff'+'/'+str(staffmember.staff_name)+'/'+str(staffmember.id)
    return redirect(urls)


def allfollowinglisttopic(request):
     if chickingvalue(request) == False: return redirect('user/login/')
     
     newtopicfllowing = FollowingNewsTopic.objects.all().filter(User__username=request.user.username)[::-1]
     TrendingTopicdb = TrendingTopic.objects.all()[::-1]
    
     dbcount = []
    #  print("\n\n\n\n\n")
     for x in newtopicfllowing:
         dbcount.append(x.NewsTopic)
    
     newsdb = News.objects.all().filter(Topic__in=dbcount,onlyvideo=False)[::-1]
     siz = len(newsdb)
     
     data ={
         'newtopicfllowing':newtopicfllowing,
         'TrendingTopicdb':TrendingTopicdb,
         'newsdb':newsdb,
         'siz':siz,
         'dbcount':dbcount,
         
     }
     return render(request,'page/allfollowinglisttopic.html',data)

def unfollowingnewstopicuser20(request,topic,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    Topicdb = Topic.objects.get(Topic=topic)
    try:
        bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=Topicdb.id)
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = FollowingNewsTopic.objects.create(NewsTopic=Topicdb)
        bookmarksdb.save()
        bookmarksdb.User.remove(request.user)
        bookmarksdb.save()
    return redirect('/topicfollowing/')

def followingnewstopicuser20(request,topic,id):
    if chickingvalue(request) == False: return redirect('user/login/')
    Topicdb = Topic.objects.get(Topic=topic)
    try:
        bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=Topicdb.id)
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    except:
        bookmarksdb = FollowingNewsTopic.objects.create(NewsTopic=Topicdb)
        bookmarksdb.save()
        bookmarksdb.User.add(request.user)
        bookmarksdb.save()
    return redirect('/topicfollowing/')

def followingall(request):
    if chickingvalue(request) == False: return redirect('user/login/')
    TrendingTopicdb = TrendingTopic.objects.all()[::-1]
    newsstaff = followingStaff.objects.all()
    yas = 0
    for x in newsstaff:
        for y in x.User.all():
            if y == request.user:
                 yas = 1
    


    allstaff = StaffMember.objects.all()
    data ={
         'TrendingTopicdb':TrendingTopicdb,
         'newsstaff':newsstaff,
         'allstaff':allstaff,
         'yas':yas
    }
    return render(request,'page/followingall.html',data)
    
def bookmarklist(request):
    if chickingvalue(request) == False: return redirect('user/login/')
    bookmarksall = bookmarks.objects.all()
   
    data ={
        'bookmarksall':bookmarksall
    }
    return render(request,'page/bookmarklist.html',data)



def Hindi(request,id,title):
        if chickingvalue(request) == False: return redirect('user/login/')
        UserInfodb = UserInfo.objects.all()
        newsdb = News.objects.get(id=id)
        translator = Translator()
        translated_result1 = translator.translate(newsdb.NewsTitle, src='en', dest='hi')
        newstitledb = translated_result1.text
        translated_result2 = translator.translate(remove_html_tags_bs4(newsdb.Txt), src='en', dest='hi')
        newstextdb = str(translated_result2.text).replace("& nbsp;","")
       
        
        allnewsdb = News.objects.all().filter(Journalists=newsdb.Journalists,JournalistsPermission=True,onlyvideo=False)[::-1]
        writers = StaffMember.objects.all().filter(staff_name=newsdb.Writers)
        editors = StaffMember.objects.all().filter(staff_name=newsdb.Editors)
        journalists = StaffMember.objects.all().filter(staff_name=newsdb.Journalists)
    
        multiplimageandvideo = multipleNewsImageAndVideo.objects.all().filter(news=newsdb)
    
        multiplimageandvideocount = multipleNewsImageAndVideo.objects.all().filter(news=newsdb).count()
   
        staffdb = StaffMember.objects.get(staff_name=newsdb.Journalists)
        TrendingTopicdb = TrendingTopic.objects.all()[::-1]
        yas = 0
        no = 0
        yasno =0
        followingnuber = 0
        Commenmaxnu = 0
        try:
            Commenmax = Comments.objects.all().filter(UserName=request.user).count()
            if Commenmax >= 3:
                Commenmaxnu = 1
        except:pass
        try:
            followingStaffcount = followingStaff.objects.get(StaffMemberName=staffdb)
            followingStaffcountss = followingStaffcount.User.all().count()

        except: followingStaffcountss =0
        try:
            followingstaffs = followingStaff.objects.get(StaffMemberName=staffdb)
            for x in followingstaffs.User.all():
                if x == request.user:
                    followingnuber = 1
        except:pass
        try:
            bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=newsdb.Topic)
            for x in bookmarksdb.User.all():
                if x == request.user:
                    yasno = 1
        except:pass
        try:
            Commen = Comments.objects.all().filter(news=newsdb)[::-1]
            Commencount = Comments.objects.all().filter(news=newsdb).count()

        except:
            Commen =0
            Commencount =0
        try:
            newsLikedb = newsLike.objects.get(News=newsdb.id)
            count = newsLikedb.User.all().count()
            for x in newsLikedb.User.all():
                if x == request.user:
                    yas = 1
        except:
            count= 0
            newsLikedb = []
        try:
            bookmarksdb = bookmarks.objects.get(News=newsdb.id)
            for x in bookmarksdb.User.all():
                if x == request.user:
                    no = 1

        except:pass
        if request.method == 'POST':
           comment= request.POST.get("comments")
           return redirect("/comment/"+str(comment)+"/"+str(newsdb.id))
        newsdb2 = News.objects.all().filter(onlyvideo=False,ManagersPermission=True,EditorsPermission=True,WritersPermission=True,JournalistsPermission=True)
        five_unique_elements = random.choices(newsdb2,k=20)
        date ={
            'five_unique_elements':five_unique_elements,
            'newsdb':newsdb,
            'staffdb':staffdb,
            'TrendingTopicdb':TrendingTopicdb,
            'count':count,
            'newsLikedb':newsLikedb,
            'yas':yas,
            'no':no,
            'Commen':Commen,
            'UserInfodb':UserInfodb,
            'Commencount':Commencount,
            'yasno':yasno,
            "followingnuber":followingnuber,
            "followingStaffcountss":followingStaffcountss,
            'Commenmaxnu':Commenmaxnu,
            'multiplimageandvideo':multiplimageandvideo,
            "multiplimageandvideocount":multiplimageandvideocount,
            'allnewsdb':allnewsdb,
            'writers':writers,
            'editors':editors,
            'journalists':journalists,
            "newstitledb":newstitledb,
            "newstext":newstextdb,
        }
        return render(request,'page/Hindi.html',date)
    
def Gujarati(request,id,title):
        if chickingvalue(request) == False: return redirect('user/login/')
        UserInfodb = UserInfo.objects.all()
        newsdb = News.objects.get(id=id)
        translator = Translator()
        translated_result1 = translator.translate(newsdb.NewsTitle, src='en', dest='gu')
        newstitledb = translated_result1.text
        translated_result2 = translator.translate(remove_html_tags_bs4(newsdb.Txt), src='en', dest='gu')
        newstextdb = str(translated_result2.text).replace("& nbsp;","")
       
        
        allnewsdb = News.objects.all().filter(Journalists=newsdb.Journalists,JournalistsPermission=True,onlyvideo=False)[::-1]
        writers = StaffMember.objects.all().filter(staff_name=newsdb.Writers)
        editors = StaffMember.objects.all().filter(staff_name=newsdb.Editors)
        journalists = StaffMember.objects.all().filter(staff_name=newsdb.Journalists)
    
        multiplimageandvideo = multipleNewsImageAndVideo.objects.all().filter(news=newsdb)
    
        multiplimageandvideocount = multipleNewsImageAndVideo.objects.all().filter(news=newsdb).count()
   
        staffdb = StaffMember.objects.get(staff_name=newsdb.Journalists)
        TrendingTopicdb = TrendingTopic.objects.all()[::-1]
        yas = 0
        no = 0
        yasno =0
        followingnuber = 0
        Commenmaxnu = 0
        try:
            Commenmax = Comments.objects.all().filter(UserName=request.user).count()
            if Commenmax >= 3:
                Commenmaxnu = 1
        except:pass
        try:
            followingStaffcount = followingStaff.objects.get(StaffMemberName=staffdb)
            followingStaffcountss = followingStaffcount.User.all().count()

        except: followingStaffcountss =0
        try:
            followingstaffs = followingStaff.objects.get(StaffMemberName=staffdb)
            for x in followingstaffs.User.all():
                if x == request.user:
                    followingnuber = 1
        except:pass
        try:
            bookmarksdb = FollowingNewsTopic.objects.get(NewsTopic=newsdb.Topic)
            for x in bookmarksdb.User.all():
                if x == request.user:
                    yasno = 1
        except:pass
        try:
            Commen = Comments.objects.all().filter(news=newsdb)[::-1]
            Commencount = Comments.objects.all().filter(news=newsdb).count()

        except:
            Commen =0
            Commencount =0
        try:
            newsLikedb = newsLike.objects.get(News=newsdb.id)
            count = newsLikedb.User.all().count()
            for x in newsLikedb.User.all():
                if x == request.user:
                    yas = 1
        except:
            count= 0
            newsLikedb = []
        try:
            bookmarksdb = bookmarks.objects.get(News=newsdb.id)
            for x in bookmarksdb.User.all():
                if x == request.user:
                    no = 1

        except:pass
        if request.method == 'POST':
           comment= request.POST.get("comments")
           return redirect("/comment/"+str(comment)+"/"+str(newsdb.id))
        newsdb2 = News.objects.all().filter(onlyvideo=False,ManagersPermission=True,EditorsPermission=True,WritersPermission=True,JournalistsPermission=True)
        five_unique_elements = random.choices(newsdb2,k=20)
        date ={
            'newsdb':newsdb,
            'staffdb':staffdb,
            'TrendingTopicdb':TrendingTopicdb,
            'count':count,
            'newsLikedb':newsLikedb,
            'yas':yas,
            'no':no,
            'Commen':Commen,
            'UserInfodb':UserInfodb,
            'Commencount':Commencount,
            'yasno':yasno,
            "followingnuber":followingnuber,
            "followingStaffcountss":followingStaffcountss,
            'Commenmaxnu':Commenmaxnu,
            'multiplimageandvideo':multiplimageandvideo,
            "multiplimageandvideocount":multiplimageandvideocount,
            'allnewsdb':allnewsdb,
            'writers':writers,
            'editors':editors,
            'journalists':journalists,
            "newstitledb":newstitledb,
            "newstext":newstextdb,
            'five_unique_elements':five_unique_elements
        }
        return render(request,'page/Gujarati.html',date)
    
    
def about_us(request):
    return render(request,'page/aboutus.html')
 

def ContactUs(request):
    return redirect("/")
    
    