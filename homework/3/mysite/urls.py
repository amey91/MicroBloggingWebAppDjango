from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^polls/', include('polls.urls')),
    url(r'^', include('grumblr.urls')),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^calc/', include('calc.urls')),
	#url(r'^calculator/', include('calculator.urls')),
	url(r'^calfinal/', include('calfinal.urls')),
	url(r'^grumblr/', include('grumblr.urls')),
	
)

