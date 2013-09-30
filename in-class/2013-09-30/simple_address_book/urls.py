from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'simple_address_book.views.home', name='home'),
    url(r'^add-entry', 'simple_address_book.views.add_entry', name='add'),
    url(r'^edit-entry/(?P<id>\d+)$', 'simple_address_book.views.edit_entry', name='edit'),
    url(r'^photo/(?P<id>\d+)$', 'simple_address_book.views.get_photo', name='photo'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'simple-address-book/login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register$', 'simple_address_book.views.register', name='register'),
)
