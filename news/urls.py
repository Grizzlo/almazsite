from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^(?P<article_id>\d+)/$', views.article, name='article'),
]
