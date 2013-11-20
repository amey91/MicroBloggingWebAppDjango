from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'charts.views.bargraph'),
	url(r'^bargraph$', 'charts.views.bargraph'),
	url(r'^svg$', 'charts.views.svg'),
	url(r'^svggraph$', 'charts.views.svggraph'),
	url(r'^svggraph2$', 'charts.views.svggraph2'),
	url(r'^githubgraph$', 'charts.views.githubgraph'),
)
