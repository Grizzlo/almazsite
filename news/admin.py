from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from news.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','text','date','image')
    fieldsets = (
        (_("Title"), {'fields': ['title_%s' % lang_code for lang_code, lang_name in settings.LANGUAGES]}),
        (_("Text"), {'fields': ['text_%s' % lang_code for lang_code, lang_name in settings.LANGUAGES]}),
        (None, {'fields': ['date', 'image']}),
    )
    list_filter = ('date',)

admin.site.register(Article, ArticleAdmin)
