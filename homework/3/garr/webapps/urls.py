from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

# Default URL routes file for the controller.  Here we are simply matching
# URL patterns by regular expression, and choosing the actual route by
# including the appropriate route file for each application.
urlpatterns = patterns('',
    url(r'^intro/', include('intro.urls')),
    url(r'^shared-todo-list/', include('shared_todo_list.urls')),
    url(r'^private-todo-list/', include('private_todo_list.urls')),
    url(r'^admin/', include(admin.site.urls)),
	
)
