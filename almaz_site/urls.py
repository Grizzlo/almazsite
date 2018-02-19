"""almaz_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, { 'next_page': '/', }, name='logout'),
    url(r'^contacts/$',views.cont, name='cont'),
    url(r'^rooms/$',views.rooms, name='rooms'),
    url(r'^services/$',views.services, name='services'),
    url(r'^$', views.index, name='index'),
    url(r'^almaz-tour/$',views.almaz_tour, name='almaz_tour'),
    url(r'^almaz-plus/$',views.almaz_plus, name='almaz_plus'),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^form/', include('forms.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    url(r'^form/', include('forms.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^news/', include('newss.urls')),
"""
urlpatterns = i18n_patterns (
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, { 'next_page': '/', }, name='logout'),
    url(r'^contacts/$',views.cont, name='cont'),
    url(r'^rooms/$',views.rooms, name='rooms'),
    url(r'^services/$',views.services, name='services'),
    url(r'^$', views.index, name='index'),
    url(r'^almaz-tour/$',views.almaz_tour, name='almaz_tour'),
    url(r'^almaz-plus/$',views.almaz_plus, name='almaz_plus'),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^form/', include('forms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'gallery.views.handler404'
