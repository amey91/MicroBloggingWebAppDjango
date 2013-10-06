from django.conf.urls import patterns, include, url

# Generates the routes for the Controller.
# Typical use is a regular expression for a URL pattern, and then the
# action to call to process requests for that URL pattern.
urlpatterns = patterns('',
    url(r'^$', 'grumblr.views.index'),
    
	url(r'^mygrumblrs$', 'grumblr.views.mygrumblrs'),
	url(r'^mygrumblrs/$', 'grumblr.views.mygrumblrs'),
	url(r'^profile/$', 'grumblr.views.profile'),
    url(r'^profile/(?P<uname>\w+)/$', 'grumblr.views.profile1'),
	url(r'^editprofile$', 'grumblr.views.editprofile'),
    url(r'^creategrumbl$', 'grumblr.views.creategrumbl'),
	url(r'^register$', 'grumblr.views.register'),
	url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'grumblr/signin.html'}),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^main$', 'grumblr.views.main'),
    url(r'^allgrumblrs$', 'grumblr.views.allgrumblrs'),
    url(r'^searchgrumblrs$', 'grumblr.views.searchgrumblrs'),
    url(r'^editprofilesubmit', 'grumblr.views.editprofilesubmit'),
    url(r'^changepassword', 'grumblr.views.changepassword'),
    url(r'^temp', 'grumblr.views.temp'),
    url(r'^temp2', 'grumblr.views.temp2'),
    url(r'^follow', 'grumblr.views.follow'),
    url(r'^findgrumblrs', 'grumblr.views.findgrumblrs'),
    url(r'^becomefollower', 'grumblr.views.becomefollower'),
    url(r'^add_comment/(?P<commentid>\d+)/$', 'grumblr.views.add_comment'),
    url(r'^blockuser', 'grumblr.views.blockuser'),
    url(r'^blockuser/', 'grumblr.views.blockuser'),
    url(r'^dislike_grumbl/(?P<commentid>\d+)/$', 'grumblr.views.dislikegrumbl'),

    
)
