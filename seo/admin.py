from django.contrib import admin
from seo.models import SeoModel
# Register your models here.
class SeoAdmin(admin.ModelAdmin):
    list_display = ('page_name_uk', 'page_name_en', 'page_name_ru', 'seo_title_uk', 'seo_title_en', 'seo_title_ru', 'seo_description_uk', 'seo_description_en', 'seo_description_ru', 'seo_keywords_uk', 'seo_keywords_en', 'seo_keywords_ru')

admin.site.register(SeoModel, SeoAdmin)
