from django.db import models
from home.models import News
# Create your models here.

# pip install django-ckeditor-5
# Add to INSTALLED_APPS:
# python
# Copy code
# INSTALLED_APPS = [
#     ...
#     "django_ckeditor_5",
# ]

class News_hindi(models.Model):
    News = models.OneToOneField(News,  on_delete=models.CASCADE)
    NewsTitle = models.CharField(max_length=250)
    Txt =   models.TextField()
    def __str__(self):
        return self.NewsTitle

class News_gujarati(models.Model):
    News = models.OneToOneField(News,  on_delete=models.CASCADE)
    NewsTitle = models.CharField(max_length=250)
    Txt =   models.TextField()
    def __str__(self):
        return self.NewsTitle

