from django.shortcuts import render,render_to_response
from news.models import Article
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.utils import translation
from seo.models import SeoModel
# Create your views here.
def news(request):
        page_id = 'News'
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
        return render(request, 'news.html', {'news': Article.objects.all(), 'seo_title':seo_title, 'seo_description': seo_description, 'seo_keywords': seo_keywords, 'lang':lang})

def article(request, article_id=1):

    return render(request, 'article.html', {'article': Article.objects.get(id=article_id)})
