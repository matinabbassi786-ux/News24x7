from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StaffMember,messengStaff
from datetime import date, timedelta
from home.models import News,Topic,multipleNewsImageAndVideo,followingStaff,TrendingTopic
from customer.models import UserInfo,UserOTP
from django.contrib.auth.models import User,Group
from .forms import NewsImagedb,multipleNewsImageAndVideodbform,Usercreated
import os
import random
import string
from customer.forms import RegisterForm,UserInfoForm
from .forms import StaffMemberdb
from customer.forms import RegisterForm
from customer.models import UserInfo

def index(request):
    if request.user.is_staff == False:return redirect('/')
    today = date.today()
    newsallgb  = News.objects.all()[::-1]
    userdb = StaffMember.objects.get(user=request.user)
    meaxax = messengStaff.objects.all().filter(OthrtUserName=userdb)
    
    if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists']:
        newsgb = News.objects.all().filter(Journalists=userdb,JournalistsPermission=True)
        newsallgb  = News.objects.all().filter(Journalists=userdb,JournalistsPermission=None)[::-1]
       
    
    
    if userdb.position in ["SeniorEditors","JuniorEditors","Editors"]:
        newsgb = News.objects.all().filter(Editors=userdb,EditorsPermission=True)
        newsallgb =  News.objects.all().filter(Editors=None,EditorsPermission=None,WritersPermission=True,JournalistsPermission=True)[::-1]
    
    if userdb.position in ["Scriptwriters","Seniorwriters","Juniorwriters"]:
        newsgb = News.objects.all().filter(Writers=userdb,WritersPermission=True)
        newsallgb =  News.objects.all().filter(JournalistsPermission=True,Writers=None)
    if userdb.position in ["Manager","CEO"]:
        newsgb = News.objects.all().filter(Writers=userdb,WritersPermission=True)
        newsallgb =  News.objects.all().filter(JournalistsPermission=True,WritersPermission=True,EditorsPermission=True)[::-1]
    

    try:
        previous_date = today - timedelta(days=0)
        data1 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday1 = previous_date.strftime("%Y-%b-%d")
        previous_date = today - timedelta(days=1)
        data2 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday2 = previous_date.strftime("%Y-%b-%d")
        previous_date = today - timedelta(days=2)
        data3 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday3 = previous_date.strftime("%Y-%b-%d")
        previous_date = today - timedelta(days=3)
        data4 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday4 = previous_date.strftime("%Y-%b-%d")
        previous_date = today - timedelta(days=4)
        data5 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday5 = previous_date.strftime("%Y-%b-%d")
        previous_date = today - timedelta(days=5)
        data6 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday6 = previous_date.strftime("%Y-%b-%d")
        previous_date = today - timedelta(days=5)
        data7 = newsgb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
        dataday7 = previous_date.strftime("%Y-%b-%d")
    except:
        newsgb = ""
        data1 = 0
        data2 = 0
        data3 = 0
        data4 = 0
        data5 = 0
        data6 = 0
        data7 = 0
        dataday1 = 'none'
        dataday2 = 'none'
        dataday3 = 'none'
        dataday4 = 'none'
        dataday5 = 'none'
        dataday6 = 'none'
        dataday7 = 'none'
        
    
    data ={
        'meaxax':meaxax,
        'userdb':userdb,
        'newsgb':newsgb,
        'data1':data1,
        'dataday1':dataday1,
        'data2':data2,
        'dataday2':dataday2,
        'data3':data3,
        'data4':data4,
        'dataday3':dataday3,
        'dataday4':dataday4,
        'data5':data5,
        'dataday5':dataday5,
        'data6':data6,
        'dataday6':dataday6,
        'data7':data7,
        'dataday7':dataday7,
        "newsallgb":newsallgb,

    }
    return render(request ,'staff/index.html',data)


def newsvewsq(request,id,slug):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    newsdb = News.objects.get(id=id)
    mutple = multipleNewsImageAndVideo.objects.all().filter(news=newsdb)
    data ={
        "userdb":userdb,
        'newsdb':newsdb,
        'mutple':mutple
    }
    return render(request ,'staff/newsvewsq.html',data)

def datalist(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    newsgb =''
    
    if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists',"Journalists"]:
        newsgb = News.objects.all().filter(Journalists=userdb)

        qadqw =['Seniorwriters','writers','Juniorwriters']
        userdball = StaffMember.objects.all().filter(position__in=qadqw)
        random_element = random.choice(userdball)
        if request.method == 'POST':
            NotSubmit = request.POST.getlist("NotSubmit")
            action = request.POST.get("action")
            Rejected = request.POST.getlist("Rejected")
            action2 = request.POST.get("action2")

            if action2 == '1':
                for x in Rejected:
                    newsdb = News.objects.get(id=int(x))
                    newsdb.delete()
                return redirect('/panelstaff/data/list/')
            if action2 == '2':
                for x in Rejected:
                    newsdb = News.objects.get(id=int(x))
                    newsdb.JournalistsPermission = None
                    newsdb.save()
                return redirect('/panelstaff/data/list/')
            
            if action == '1':
                for x in NotSubmit:
                    newsdb = News.objects.get(id=int(x))
                    newsdb.JournalistsPermission = True
                    newsdb.Writers =random_element
                    newsdb.save()
                return redirect('/panelstaff/data/list/')
            if action == '2':
                for x in NotSubmit:
                    newsdb = News.objects.get(id=int(x))
                    newsdb.JournalistsPermission = False
                    newsdb.save()
                return redirect('/panelstaff/data/list/')
           
        Journalistsdata = {
            'newsgb':newsgb,
            'userdb':userdb
        }
        return render(request ,'staff/Journalists.html',Journalistsdata)

    if userdb.position in ["SeniorEditors","JuniorEditors","Editors"]:
        userdb = StaffMember.objects.get(user=request.user)
        newsgb = News.objects.all().filter(Editors=userdb)
        newsgb = News.objects.all().filter(Editors=userdb,EditorsPermission=None)[::-1]
        newsgbss = News.objects.all().filter(Editors=userdb,EditorsPermission=False)[::-1]
        newsgbTrue = News.objects.all().filter(Editors=userdb,EditorsPermission=True)[::-1]
        if request.method == 'POST':
            Rejected = request.POST.getlist("Rejected")
            action = request.POST.get("action")
            action2 = request.POST.get("action2")
            Rejected1 = request.POST.getlist("Rejected1")
               
                 
            if action == '2':
                for x in Rejected:
                    qadqw =["SeniorEditors","JuniorEditors","Editors"]
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr = News.objects.get(id = int(x))
                    newsfr.Editors = random_element
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            
            if action == '1':
                for x in Rejected:
                    qadqw =["SeniorEditors","JuniorEditors","Editors"]
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr = News.objects.get(id = int(x))
                    newsfr.EditorsPermission = False
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            
            if action2 == '3':
                for x in Rejected1:
                    newsfr = News.objects.get(id = int(x))
                    qadqw =["SeniorEditors","JuniorEditors","Editors"]
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr.EditorsPermission = True
                
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            
            if action2 == '2':
                for x in Rejected1:
                    qadqw =["SeniorEditors","JuniorEditors","Editors"]
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr = News.objects.get(id = int(x))
                    newsfr.Editors = random_element
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
                
        data ={
            "userdb":userdb,
            'newsgb':newsgb,
            'newsgbss':newsgbss,
            'newsgbTrue':newsgbTrue
        }
        return render(request ,'staff/writersdb.html',data)

    
    if userdb.position in ["Scriptwriters","Seniorwriters","Juniorwriters",'writers']:
        newsgb = News.objects.all().filter(Writers=userdb,WritersPermission=None)[::-1]
        userdb = StaffMember.objects.get(user=request.user)
        newsgbss = News.objects.all().filter(Writers=userdb,WritersPermission=False)[::-1]
        newsgbTrue = News.objects.all().filter(Writers=userdb,WritersPermission=True)[::-1]
        if request.method == 'POST':
            Rejected = request.POST.getlist("Rejected")
            action = request.POST.get("action")
            action2 = request.POST.get("action2")
            Rejected1 = request.POST.getlist("Rejected1")
               
                 
            if action == '2':
                for x in Rejected:
                    qadqw =['Seniorwriters','writers','Juniorwriters']
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr = News.objects.get(id = int(x))
                    newsfr.Writers = random_element
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            
            if action == '1':
                for x in Rejected:
                    qadqw =['Seniorwriters','writers','Juniorwriters']
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr = News.objects.get(id = int(x))
                    newsfr.WritersPermission = False
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            
            if action2 == '3':
                for x in Rejected1:
                    newsfr = News.objects.get(id = int(x))
                    qadqw =['SeniorEditors','Editors','JuniorEditors']
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr.WritersPermission = True
                    newsfr.Editors = random_element
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            
            if action2 == '2':
                for x in Rejected1:
                    qadqw =['Seniorwriters','writers','Juniorwriters']
                    userdballs = StaffMember.objects.all().filter(position__in=qadqw)
                    random_element = random.choice(userdballs)
                    newsfr = News.objects.get(id = int(x))
                    newsfr.Writers = random_element
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
                
        data ={
            "userdb":userdb,
            'newsgb':newsgb,
            'newsgbss':newsgbss,
            'newsgbTrue':newsgbTrue
        }
        return render(request ,'staff/writersdb.html',data)
        
    if userdb.position in ["Manager","Admin","CEO"]:
        newsgb =  News.objects.all().filter(JournalistsPermission=True,WritersPermission=True,EditorsPermission=True,ManagersPermission=None)[::-1]
        newsTruegb =  News.objects.all().filter(JournalistsPermission=True,WritersPermission=True,EditorsPermission=True,ManagersPermission=True)[::-1]
        newsFalsegb =  News.objects.all().filter(JournalistsPermission=True,WritersPermission=True,EditorsPermission=True,ManagersPermission=False)[::-1]
        if request.method == 'POST':
            Rejected1 = request.POST.getlist("Rejected")
            action = request.POST.get("action")
            action2 = request.POST.get("action2")
            Rejected2 = request.POST.getlist("Rejected2")
            
            if action2 == '1':
                for x in Rejected2:
                    newsfr = News.objects.get(id = int(x))
                    newsfr.ManagersPermission = True
                    newsfr.save()
                return redirect('/panelstaff/data/list/')

            if action == '1':
                for x in Rejected1:
                    newsfr = News.objects.get(id = int(x))
                    newsfr.ManagersPermission = True
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
            if action == '2':
                for x in Rejected1:
                    newsfr = News.objects.get(id = int(x))
                    newsfr.ManagersPermission = False
                    newsfr.save()
                return redirect('/panelstaff/data/list/')
        data ={
            'userdb':userdb,
            'newsgb':newsgb,
            'newsFalsegb':newsFalsegb,
            'newsTruegb':newsTruegb
        }
        return render(request ,'staff/Manager.html',data)
   


    data ={
        'userdb':userdb,
        
        }
    return  redirect("/")


def multipleimedit(request,id,news):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    multiple = multipleNewsImageAndVideo.objects.get(id=id)
    multipleNewsImageAndVideodbformdb = multipleNewsImageAndVideodbform(request.POST, request.FILES, instance=multiple )
    newsdb = News.objects.get(id=news)
    if request.method == 'POST':
        multipleNewsImageAndVideodbformdb = multipleNewsImageAndVideodbform(request.POST, request.FILES, instance=multiple )
        if multipleNewsImageAndVideodbformdb.is_valid():
            multipleNewsImageAndVideodbformdb.save()
            urls = f'/panelstaff/editnews/{newsdb.slug}/{newsdb.id}'
            return redirect(urls)

    data ={
        'userdb':userdb,
        'multipleNewsImageAndVideodbformdb':multipleNewsImageAndVideodbformdb,
        'multiple':multiple
    }
    return render(request ,'staff/multipleNewsImageAndVideo.html',data)
   

def editnews(request,slug,id):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    newsdb = News.objects.get(id=id)
    topic =  Topic.objects.all()
    multipleNewsImageAndVideodb= multipleNewsImageAndVideo.objects.all().filter(news=newsdb)
    NewsImagedbform = NewsImagedb(request.POST, request.FILES, instance=newsdb)
    topicdb  =request.POST.get('topic')
    Titledb  =request.POST.get('Title')
    onlyvideo  =request.POST.get('onlyvideo')
   
        
    explaineddb  = request.POST.get('explaine')
    if request.method == 'POST':
        onlyvideo  =request.POST.get('onlyvideo')
        qur = False
        if onlyvideo == "on":
            qur = True      
            
        topicdb  =request.POST.get('topic')
        Titledb  =request.POST.get('Title')
        explaineddb  = request.POST.get('explaine')
        NewsImagedbform = NewsImagedb(request.POST, request.FILES, instance=newsdb)
        topicalldb = Topic.objects.get(id=topicdb)
        newsdb.Txt = explaineddb
        newsdb.Topic = topicalldb
        newsdb.NewsTitle = Titledb
        newsdb.onlyvideo = qur
        newsdb.save()
        newsdb.clean()
        if NewsImagedbform.is_valid():
            NewsImagedbform.save()
            return redirect("/panelstaff/data/list/")

    data ={
        'userdb':userdb,
        'newsdb':newsdb,
        'topic':topic,
        'NewsImagedbform':NewsImagedbform,
        'multipleNewsImageAndVideodb':multipleNewsImageAndVideodb,
       
        
        
    }
    return render(request,'staff/editnews.html',data)


def creatdbtbale(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    data ={
    'userdb':userdb,
    }
    return render(request,'staff/creatdbtbale.html',data)
   

def Newsdbcreats(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists']:
        def coverttolist(qrdel):
            qurd =[]
            for x in qrdel:
                qurd.append(x)
            return qurd

        b = coverttolist(string.ascii_lowercase)
        c = coverttolist(string.ascii_uppercase)
        d = coverttolist(string.digits)

        random_five_unique2 = random.choices(b,k=40)
        random_five_unique3 = random.choices(c,k=40)
        random_five_unique4 = random.choices(d,k=40)
        sfsfpo0 = random.randint(100,99999)
        astr = "code="+str(sfsfpo0)+"&"
        for x in range(0,20) :
            astr += random_five_unique2[x]+random_five_unique3[x]+random_five_unique4[x]
    
        Nain = News.objects.create(Topic=None,Journalists=userdb,Writers=None,Editors =None, NewsTitle =astr, Txt =astr, Image =None, Video =None)
        Nain.save()
        for fruit in range(0,3):
            kqdbnqn = multipleNewsImageAndVideo.objects.create(news=Nain,image=None ,video=None)
            kqdbnqn.save()

        qadqd = News.objects.get(id=Nain.id)
        qadqd.NewsTitle ="Enter Hare"
        qadqd.Txt = "Enter Hare"
        qadqd.save()


        return redirect("/panelstaff/data/list/")
    else:
         return redirect("/panelstaff/data/list/")
 

def topicecreatdb(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    topich =  request.POST.get("topic")
    if request.method == 'POST':
        qdqd= Topic.objects.create(Topic=topich,CreatedBy=userdb)
        qdqd.save()
        return redirect("/panelstaff/")

    data ={
        'userdb':userdb,
    }
    return render(request,'staff/topicecreatdb.html',data)
    


def Writersrandom(request,id):
    if request.user.is_staff == False:return redirect('/')
    Newsdb = News.objects.get(id=id)
    qadqw =['Seniorwriters','writers','Juniorwriters']
    userdball = StaffMember.objects.all().filter(position__in=qadqw)
    random_element = random.choice(userdball)
    Newsdb.Writers = random_element
    Newsdb.save()
    return redirect("/panelstaff/data/list/")

def Writerssomeone(request,id):
    if request.user.is_staff == False:return redirect('/')
    Newsdb = News.objects.get(id=id)
    qadqw =['Seniorwriters','writers','Juniorwriters']
    userdball = StaffMember.objects.all().filter(position__in=qadqw)
    userdb = StaffMember.objects.get(user=request.user)
    yas = 1
    data ={
        'userdb':userdb,
        'userdball':userdball,
        'Newsdb':Newsdb,
        'yas':yas
    }
    return render(request,'staff/Writerssomeone.html',data)
 

def somewriter(request,id,name,id2):
    if request.user.is_staff == False:return redirect('/')
    newsdb = News.objects.get(id=id)
    userdb = StaffMember.objects.get(id=id2)
    newsdb.Writers = userdb
    newsdb.save()
    return redirect("/panelstaff/data/list/")


def editorsrandom(request,id):
    if request.user.is_staff == False:return redirect('/')
    Newsdb = News.objects.get(id=id)
    qadqw =['SeniorEditors','Editors','JuniorEditors']
    userdball = StaffMember.objects.all().filter(position__in=qadqw)
    random_element = random.choice(userdball)
    Newsdb.Editors = random_element
    Newsdb.save()
    return redirect("/panelstaff/data/list/")

def editorsomeone(request,id):
    if request.user.is_staff == False:return redirect('/')
    Newsdb = News.objects.get(id=id)
    qadqw = ['SeniorEditors','Editors','JuniorEditors']
    userdball = StaffMember.objects.all().filter(position__in=qadqw)
    userdb = StaffMember.objects.get(user=request.user)
    yas = 0
    data ={
        'userdb':userdb,
        'userdball':userdball,
        'Newsdb':Newsdb,
        'yas':yas
    }
    return render(request,'staff/Writerssomeone.html',data)

def editorsome(request,id,name,id2):
    if request.user.is_staff == False:return redirect('/')
    newsdb = News.objects.get(id=id)
    userdb = StaffMember.objects.get(id=id2)
    newsdb.Editors = userdb
    newsdb.save()
    return redirect("/panelstaff/data/list/")


def uservews(request,name,id):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    mainuserdb = StaffMember.objects.get(id=id)
    try:
        totles = followingStaff.objects.get(id=id)
        totl = totles.User.all().count()
    except:
        totl =0
    
    if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists']:
        newsdb = News.objects.all().filter(Journalists=mainuserdb)[::-1]
        newsdbtotle = News.objects.all().filter(Journalists=mainuserdb).count()

    elif userdb.position in ["Scriptwriters","Seniorwriters","Juniorwriters",'writers']:
           newsdb  = News.objects.all().filter(Writers=mainuserdb)[::-1]
           newsdbtotle  = News.objects.all().filter(Writers=mainuserdb).count()

    elif userdb.position in ['SeniorEditors','Editors','JuniorEditors']:
         newsdb = News.objects.all().filter(Editors=mainuserdb)[::-1]
         newsdbtotle = News.objects.all().filter(Editors=mainuserdb).count()
    else:
        newsdb = ""
        newsdbtotle=0
    
    sandrv = request.POST.get('Send')
    Messagev = request.POST.get('Message')
    if request.method == "POST":
        sandrv = request.POST.get('Send')
        Messagev = request.POST.get('Message')
        mainswe = messengStaff.objects.create(
            user=userdb,
            OthrtUserName=mainuserdb,
            Txt = Messagev
            )
        mainswe.save()
     


    data ={
        'userdb':userdb,
        'mainuserdb':mainuserdb,
        'totl':totl,
        'newsdb':newsdb,
        'newsdbtotle':newsdbtotle
    }
    return render(request,'staff/uservews.html',data)
   




def Statistics(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    
    if userdb.position in ["Admin","CEO","Manager"]:
        return redirect('Statisticsceo')
        
    if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists','Journalists']:
        newsdb = News.objects.all().filter(Journalists=userdb)


        
    if userdb.position in ["Scriptwriters","Seniorwriters","Juniorwriters",'writers']:
        newsdb = News.objects.all().filter(Writers=userdb)
         
    if userdb.position in ["SeniorEditors","JuniorEditors","Editors"]:
            newsdb = News.objects.all().filter(Editors=userdb)

    today = date.today()
    dbnewsn1 =[]
    dbdate1 =[]
    dbnewsn2 =[]
    dbdate2 =[]
   
    try:
        for x in range(0,366):
            previous_date = today - timedelta(days=x)
            data1 = newsdb.filter(CreatDate=previous_date.strftime("%Y-%m-%d")).count()
            dbnewsn1.append(data1)
            dbdate1.append(previous_date.strftime("%Y-%m-%d"))
        
        for x in range(0,366):
            if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists','Journalists']:
                data1 = newsdb.filter(CreatDate=previous_date.strftime("%Y-%m-%d"), JournalistsPermission = True).count()
            if userdb.position in ["Scriptwriters","Seniorwriters","Juniorwriters","writers"]:
                data1 = newsdb.filter(CreatDate=previous_date.strftime("%Y-%m-%d"), WritersPermission = True).count()
            
            if userdb.position in ["SeniorEditors","JuniorEditors","Editors"]:
                data1 = newsdb.filter(CreatDate=previous_date.strftime("%Y-%m-%d"), EditorsPermission = True).count()
            

            
            previous_date = today - timedelta(days=x)
            dbnewsn2.append(data1)
            dbdate2.append(previous_date.strftime("%Y-%m-%d"))
        
    except:pass

  
    



    data = {
        'userdb':userdb,
        'dbnewsn1':dbnewsn1,
        'dbdate1':dbdate1,
        'dbnewsn2':dbnewsn2,
        'dbdate2':dbdate2

    }
    return render(request,'staff/Statistics.html',data)
    




def Statisticsceo(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    if userdb.position not in ["Admin","CEO","Manager"]:return redirect('/')

    Malecount = UserInfo.objects.all().filter(Ganders='Male').count()
    Femalecount = UserInfo.objects.all().filter(Ganders='Female').count()
    Othercount = UserInfo.objects.all().filter(Ganders='Other').count()
    UserOTPTruecount = UserOTP.objects.all().filter(is_email_verified=True).count()
    Usercount = User.objects.all().count()
    Staffcount = StaffMember.objects.all().count()
    totlenewscount = News.objects.all().count()
    Journalistssubmit = News.objects.all().filter(JournalistsPermission=True).count()
    Writerscount = News.objects.all().exclude(Writers=None).count()
    Writerssubmit = News.objects.all().filter(WritersPermission=True).count()
    Editorscount = News.objects.all().exclude(Editors=None).count()
    Topiccount = Topic.objects.all().count()
    TrendingTopiccount = TrendingTopic.objects.all().count()
    Editorssubmit  = News.objects.all().filter(EditorsPermission = True).count()
    Managerssubmit  = News.objects.all().filter(ManagersPermission = True).count()

    

    data = {
        'userdb':userdb,
        'Malecount':Malecount,
        'Femalecount':Femalecount,
        'Othercount':Othercount,
        'UserOTPTruecount':UserOTPTruecount,
        'Usercount':Usercount,
        'Staffcount':Staffcount,
        'totlenewscount':totlenewscount,
        'Journalistssubmit':Journalistssubmit,
        'Writerscount':Writerscount,
        'Writerssubmit':Writerssubmit,
        'Editorscount':Editorscount,
        'Editorssubmit':Editorssubmit,
        'Managerssubmit':Managerssubmit,
        'Topiccount':Topiccount,
        'TrendingTopiccount':TrendingTopiccount
    }
    return render(request,'staff/Statisticsceo.html',data)



def History(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    topic = Topic.objects.all().filter(CreatedBy=userdb)[::-1]
    
    if userdb.position in ['SpecialReporters','SeniorReporters','JuniorReporters','SpecialJournalists','SeniorJournalists','JuniorJournalists','Journalists']:
        newsdb = News.objects.all().filter(Journalists=userdb)[::-1]


        
    if userdb.position in ["Scriptwriters","Seniorwriters","Juniorwriters",'writers']:
        newsdb = News.objects.all().filter(Writers=userdb)[::-1]
         
    if userdb.position in ["SeniorEditors","JuniorEditors","Editors"]:
            newsdb = News.objects.all().filter(Editors=userdb)[::-1]
    if userdb.position in ["Admin","CEO","Manager"]:
         newsdb = News.objects.all()[::-1]
         topic = Topic.objects.all().filter(CreatedBy=userdb)[::-1]
    data = {
        'userdb':userdb,
        'newsdb':newsdb,
        'topic':topic
    }
    return render(request,'staff/History.html',data)
    



def Messages(request):
    if request.user.is_staff == False:return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    meaxax = messengStaff.objects.all().filter(OthrtUserName=userdb)[::-1]
    data ={
        'userdb':userdb,
        'meaxax':meaxax
    }
    return render(request,'staff/Messages.html',data)
   





def StaffAll(request):
    if userdb.position  not in ["Admin","CEO","Manager"]: return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    Staffall  = StaffMember.objects.all()[::-1]
    data ={
        'userdb':userdb,
        'Staffall':Staffall
    }
    return render(request,'staff/StaffAll.html',data)
   

def Staffadd(request):
    if userdb.position  not in ["Admin","CEO","Manager"]: return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    a1 = StaffMemberdb(request.POST, request.FILES)

    if request.method == 'POST':
        a1 = StaffMemberdb(request.POST, request.FILES)
        if a1.is_valid():
            a1.save()
            


    data={
        'userdb':userdb,
        'a1':a1,

    }
    return render(request,'staff/Staffadd.html',data)



def Staffcreate(request):
    if userdb.position  not in ["Admin","CEO","Manager"]: return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    forms = StaffMemberdb()
    forms2 = RegisterForm()

    
    if request.method == 'POST':
        forms2 = RegisterForm(request.POST)
        if forms2.is_valid():
            usernamedb =  forms2.cleaned_data['username']
            forms2.save()
            url = str('/panelstaff/creatStaff/'+usernamedb)
            return redirect(url)
    data ={
        'userdb':userdb,
        'forms':forms,
        'forms2':forms2,
    }
    return render(request,'staff/Staffcreate.html',data)

def Staffcreate2(request,pk):
    if userdb.position  not in ["Admin","CEO","Manager"]: return redirect('/')
    userdb = StaffMember.objects.get(user=request.user)
    userd  = User.objects.get(username=pk)
    
    
    forms = StaffMemberdb()
    if request.method == 'POST':
            forms = StaffMemberdb(request.POST, request.FILES)
            # print(forms.clean)
            Ganders = request.POST.get("Ganders")
            print(Ganders)
            if forms.is_valid():
               use = UserInfo.objects.create(UserName=userd,Ganders=Ganders)
               use.save()
               forms.save()
               userd.is_staff = True
               userd.save()
               return redirect("/staff/")
            else:
                print(forms.errors)
            

    data ={
        'forms':forms,
        "user":userd
    }
    return render(request,'staff/Staffcreate2.html',data)
