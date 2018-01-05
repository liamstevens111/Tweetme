from django.conf.urls import url

from .views import (
	TweetCreateView,
	TweetDetailView, 
	TweetListView,
	TweetUpdateView,
	TweetDeleteView
	)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name = 'list'), # /tweet/
    url(r'^create/$', TweetCreateView.as_view(), name = 'create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name = 'detail'), # /tweet/[number]/
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name = 'update'), # /tweet/[number]/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name = 'delete'), # /tweet/[number]/delete/
]