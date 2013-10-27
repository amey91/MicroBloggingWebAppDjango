from django.conf.urls import patterns, include, url

urlpatterns = patterns('private_todo_list.views',
    url(r'^$', 'home', name='home'),
    url(r'^add-item', 'add_item', name='add-item'),
    url(r'^delete-item/(?P<id>\d+)$', 'delete_item', name='delete-item'),
    url(r'^login$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^register$', 'register', name='register'),
)
