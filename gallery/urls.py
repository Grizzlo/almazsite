from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.gallery ,name="gallery"),
    #url(r'^(?P<slug>[-\w]+)$', views.AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()
]
