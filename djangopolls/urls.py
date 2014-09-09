from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^backoffice/', include(admin.site.urls)),  # admin site
    url(r'^polls/', include("polls.urls", namespace="polls")),
    url(r'^dashboard/$', 'polls.views.dashboard'),
    url(r'^thankyou/$', 'polls.views.thankyou'),
    url(r'^$', 'polls.views.home', name='home'),
) 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
