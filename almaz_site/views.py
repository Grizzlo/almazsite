from django.shortcuts import render
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation
from seo.models import SeoModel


#from django.utils import timezone

def rooms(request):
        page_id = 'Rooms'
        page_seo_data = SeoModel.objects.get(page_name_en = page_id )
        lang = translation.get_language()
        if lang == 'en' :
            seo_title = page_seo_data.seo_title_en
            seo_description = page_seo_data.seo_description_en
            seo_keywords = page_seo_data.seo_keywords_en
        elif lang == 'ru' :
            seo_title = page_seo_data.seo_title_ru
            seo_description = page_seo_data.seo_description_ru
            seo_keywords = page_seo_data.seo_keywords_ru
        else:
            seo_title = page_seo_data.seo_title_uk
            seo_description = page_seo_data.seo_description_uk
            seo_keywords = page_seo_data.seo_keywords_uk
        return render(request, 'rooms.html',{'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def services(request):
        page_id = 'Services'
        page_seo_data = SeoModel.objects.get(page_name_en = page_id )
        lang = translation.get_language()
        if lang == 'en' :
            seo_title = page_seo_data.seo_title_en
            seo_description = page_seo_data.seo_description_en
            seo_keywords = page_seo_data.seo_keywords_en
        elif lang == 'ru' :
            seo_title = page_seo_data.seo_title_ru
            seo_description = page_seo_data.seo_description_ru
            seo_keywords = page_seo_data.seo_keywords_ru
        else:
            seo_title = page_seo_data.seo_title_uk
            seo_description = page_seo_data.seo_description_uk
            seo_keywords = page_seo_data.seo_keywords_uk
        return render(request, 'services.html' ,{'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def almaz_plus(request):
        page_id ='Almaz-Plus'
        page_seo_data = SeoModel.objects.get(page_name_en = page_id )
        lang = translation.get_language()
        if lang == 'en' :
            seo_title = page_seo_data.seo_title_en
            seo_description = page_seo_data.seo_description_en
            seo_keywords = page_seo_data.seo_keywords_en
        elif lang == 'ru' :
            seo_title = page_seo_data.seo_title_ru
            seo_description = page_seo_data.seo_description_ru
            seo_keywords = page_seo_data.seo_keywords_ru
        else:
            seo_title = page_seo_data.seo_title_uk
            seo_description = page_seo_data.seo_description_uk
            seo_keywords = page_seo_data.seo_keywords_uk
        return render(request, 'almaz-plus.html' ,{'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def cont(request):
        page_id ='Contact-Us'
        page_seo_data = SeoModel.objects.get(page_name_en = page_id )
        lang = translation.get_language()
        if lang == 'en' :
            seo_title = page_seo_data.seo_title_en
            seo_description = page_seo_data.seo_description_en
            seo_keywords = page_seo_data.seo_keywords_en
        elif lang == 'ru' :
            seo_title = page_seo_data.seo_title_ru
            seo_description = page_seo_data.seo_description_ru
            seo_keywords = page_seo_data.seo_keywords_ru
        else:
            seo_title = page_seo_data.seo_title_uk
            seo_description = page_seo_data.seo_description_uk
            seo_keywords = page_seo_data.seo_keywords_uk
        return render(request, 'cont.html' ,{'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def index(request):
        page_id ='Almaz'
        page_seo_data = SeoModel.objects.get(page_name_en = page_id )
        lang = translation.get_language()
        if lang == 'en' :
            seo_title = page_seo_data.seo_title_en
            seo_description = page_seo_data.seo_description_en
            seo_keywords = page_seo_data.seo_keywords_en
        elif lang == 'ru' :
            seo_title = page_seo_data.seo_title_ru
            seo_description = page_seo_data.seo_description_ru
            seo_keywords = page_seo_data.seo_keywords_ru
        else:
            seo_title = page_seo_data.seo_title_uk
            seo_description = page_seo_data.seo_description_uk
            seo_keywords = page_seo_data.seo_keywords_uk
        return render(request, 'landing.html',{'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def almaz_tour(request):
        page_id ='Almaz-Tour'
        page_seo_data = SeoModel.objects.get(page_name_en = page_id )
        lang = translation.get_language()
        if lang == 'en' :
            seo_title = page_seo_data.seo_title_en
            seo_description = page_seo_data.seo_description_en
            seo_keywords = page_seo_data.seo_keywords_en
        elif lang == 'ru' :
            seo_title = page_seo_data.seo_title_ru
            seo_description = page_seo_data.seo_description_ru
            seo_keywords = page_seo_data.seo_keywords_ru
        else:
            seo_title = page_seo_data.seo_title_uk
            seo_description = page_seo_data.seo_description_uk
            seo_keywords = page_seo_data.seo_keywords_uk
        return render(request, 'almaz-tour.html',{'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})
