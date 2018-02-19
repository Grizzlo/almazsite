from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from django.utils import translation
from seo.models import SeoModel
from gallery.models import Album, AlbumImage
from django.utils.translation import LANGUAGE_SESSION_KEY


def gallery(request):
    page_id = 'Gallery'
    #page_seo_data = SeoModel.objects.get(page_name_en = page_id )
    #listCategoryTitl = Album.objects.filter(is_visible=True).order_by('-created').slug
    #listCategorySlug = Album.objects.filter(is_visible=True).order_by('-created').slug
    #listCategorySlug = Album.objects.filter(is_visible=True).order_by('-created').slug
    page_seo_data = SeoModel.objects.get(page_name_en = page_id )
    listImage = AlbumImage.objects.all()
    lang = translation.get_language()
    if lang == 'en' :
        listCategory = Album.objects.values_list('slug','title_en').filter(is_visible=True).order_by('-created')
        seo_title = page_seo_data.seo_title_en
        seo_description = page_seo_data.seo_description_en
        seo_keywords = page_seo_data.seo_keywords_en
    elif lang == 'ru' :
        listCategory = Album.objects.values_list('slug','title_ru').filter(is_visible=True).order_by('-created')
        seo_title = page_seo_data.seo_title_ru
        seo_description = page_seo_data.seo_description_ru
        seo_keywords = page_seo_data.seo_keywords_ru
    else:
        listCategory = Album.objects.values_list('slug','title').filter(is_visible=True).order_by('-created')
        seo_title = page_seo_data.seo_title_uk
        seo_description = page_seo_data.seo_description_uk
        seo_keywords = page_seo_data.seo_keywords_uk

    return render(request, 'gallery.html', { 'categories': listCategory,'images':listImage, 'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def handler404(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)
