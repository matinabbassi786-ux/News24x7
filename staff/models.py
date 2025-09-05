from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Office(models.Model):
    address = models.CharField(max_length=200,unique=True)
    manger = models.CharField(max_length=100)
    def __str__(self):
        return self.address

class StaffMember(models.Model):
    choicesPosition = (
        ("none","none"),
        ("Admin","Admin"),
        ("CEO","CEO"),
        ('Manager','Manager'),
        ("SalesManager","SalesManager"),
        ("TechicalDirectors","TechicalDirectors"),
        ("NewsDirectors","NewsDirectors"),
        ("HR","HR"),
        ("NewsAnchors","NewsAnchors"),
        ("Newsdirector","Newsdirector"),
        ("Producers","Producers"),
        
        ("Reporters","Reporters"),
        ("SeniorReporters","SeniorReporters"),
        ("JuniorReporters","JuniorReporters"),
        
        ("Journalists","Journalists"),
        ("SeniorJournalists","SeniorJournalists"),
        ("JuniorJournalists","JuniorJournalists"),
        
        ("CameraMan","CameraMan"),
        ("CameraOperators","CameraOperators"),
        ("PhotoJournalists","PhotoJournalists"),
        
        ("SeniorEditors","SeniorEditors"),
        ("Editors","Editors"),
        ("JuniorEditors","JuniorEditors"),


        ("Editors","Editors"),
        ("AudioEditors","AudioEditors"),
        ("AudioEngineer","AudioEngineer"),
        
        ("Seniorwriters","Seniorwriters"),
        ('writers','writers'),
        ("Juniorwriters","Juniorwriters"),
        
        ("AssignmentEditors","AssignmentEditors"),
        ("GraphicDesigners","GraphicDesigners"),
        ("BroadcastEngineer","BroadcastEngineer"),
        ("LightingTechnician","LightingTechnician"),
        ("GraphicDesigner","GraphicDesigner"),
        ("MakeupArtist","MakeupArtist"),
        ("TechnicalStaff","TechnicalStaff"),
        ("SupportStaff","SupportStaff"),
    )
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=200)
    Office = models.ForeignKey(Office,on_delete=models.CASCADE)
    position = models.CharField(choices=choicesPosition ,max_length=100)
    DateOfBirth = models.DateField()
    PhoneNumber = models.CharField(max_length=100)
    ZipCode = models.CharField(max_length=15)
    OneAddress = models.TextField(max_length=350)
    TwoAddress = models.TextField(max_length=350 ,blank=True,null=True)
    picture = models.FileField(upload_to="StaffMember/")
    JoinDate = models.DateField()
    LeaveDate = models.DateField(blank=True,null=True)
    aboutme = HTMLField(blank=True,null=True)
    def __str__(self):
        return self.staff_name


class messengStaff(models.Model):
    user = models.ForeignKey(StaffMember,on_delete=models.CASCADE ,related_name="User")
    OthrtUserName = models.ForeignKey(StaffMember,on_delete=models.CASCADE , related_name="OthrtUserName")
    Txt = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
   