from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^redirect-tour$', views.redirect_tour, name='redirect_tour'),
    url(r'^get_tour$', views.get_tour, name='get_tour'),
    url(r'^booking$', views.booking, name='booking'),
    url(r'^redirect-booking$', views.redirect_booking, name='redirect_booking'),
]
