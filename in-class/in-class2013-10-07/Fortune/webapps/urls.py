from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^fortune$', 'fortune.views.home', name='home'),
)
