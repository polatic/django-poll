from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^$', 'polls.views.home', name="home"),
   url(r'^dashboard/$', 'polls.views.dashboard', name="dashboard"),
   url(r'^reset/$', 'polls.views.reset', name="reset"),
   url(r'^thankyou/$', 'polls.views.thankyou', name="thankyou"),
)
