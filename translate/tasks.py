from background_task import background
from django.contrib.auth.models import User
from home.models import News
from .models import News_gujarati,News_hindi
from bs4 import BeautifulSoup
from googletrans import Translator
from textblob import TextBlob
from spellchecker import SpellChecker

spell = SpellChecker()


def en_to_gu(text:str):
    soup = BeautifulSoup(text, 'html.parser')
    translator = Translator()
    QDQDQSXQ = soup.get_text()
   
    try:
        correction = spell.correction(str(text))
        text = correction
        translation = translator.translate(str(text), src='en', dest='gu')
        text = translation.text
    except:
            text = False
    return text

def en_to_hi(text:str):
    soup = BeautifulSoup(text, 'html.parser')
    translator = Translator()
    translator = Translator()
  
    try:
        correction = spell.correction(str(text))
        text = correction
        translation = translator.translate(str(text), src='en', dest='hi')
        text = translation.text
    except:
            text = False
    return text

@background(schedule=0)
def translate_():
    News_db = News.objects.all()
    for x in News_db:
        if x.ManagersPermission == True:
            title = en_to_hi(x.NewsTitle)
            txt  = en_to_hi(x.Txt)
            if title == False :
                print(f"{x.id} Hava No hindi Title")
            else:
                print(f"{x.id} Is hindi Runging ...")
                try:
                    hindi = News_hindi.objects.create(News=x,NewsTitle=title,Txt=txt)
                    hindi.save()
                    print(f"{x.id} Is Done hindi")
                except:pass
            title = en_to_gu(x.NewsTitle)
            txt  = en_to_gu(x.Txt)
            if title == False :
                print(f"{x.id} Hava No gujarati Title")
            else:
                print(f"{x.id} Is gujarati Runging ...")
                try:
                    hindi = News_gujarati.objects.create(News=x,NewsTitle=title,Txt=txt)
                    hindi.save()
                    print(f"{x.id} Is Done gujarati ")
                except:pass
                    



# @background(schedule=0)
# def :
#     News_db = News.objects.all()
#     for x in News_db:
#         if x.ManagersPermission == True:
#             title = en_to_gu(x.NewsTitle)
#             txt  = en_to_gu(x.Txt)
#             if title == False :
#                 print(f"{x.id} {x.NewsTitle}Soryy")
#             else:
#                 try:
#                     gujarati = News_gujarati.objects.create(News=x,NewsTitle=title,Txt=txt)
#                     gujarati.save()
#                     print(f"{x.id} gujarati done............")
#                 except:pass
#             title = en_to_hi(x.NewsTitle)
#             txt  = en_to_hi(x.Txt)
#             if title == False and txt == False :
#                 print("Soryy")
#             else:
#                 try:
#                     gujarati = News_hindi.objects.create(News=x,NewsTitle=title,Txt=txt)
#                     gujarati.save()
#                     print(f"{x.id}hindi done............")
#                 except:pass
            