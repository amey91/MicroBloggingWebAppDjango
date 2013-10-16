from django.conf.urls import patterns, include, url

urlpatterns = patterns('uni.views',
    url(r'^$', 'home', name='home'),
    url(r'^get-students$', 'get_students', name='get_students'),
)
