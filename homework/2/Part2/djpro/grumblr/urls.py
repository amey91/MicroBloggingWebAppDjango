from django.conf.urls import patterns, include, url

# Generates the routes for the Controller.
# Typical use is a regular expression for a URL pattern, and then the
# action to call to process requests for that URL pattern.
urlpatterns = patterns('',
    url(r'^$', 'grumblr.views.index'),
    
	url(r'^mygrumblrs$', 'grumblr.views.mygrumblrs'),
	url(r'^mygrumblrs/$', 'grumblr.views.mygrumblrs'),
	url(r'^profile$', 'grumblr.views.profile'),
	url(r'^editprofile$', 'grumblr.views.editprofile'),
    url(r'^creategrumbl$', 'grumblr.views.creategrumbl'),
	url(r'^register$', 'grumblr.views.register'),
	url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'grumblr/signin.html'}),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
)
