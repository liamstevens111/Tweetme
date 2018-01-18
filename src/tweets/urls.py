from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
	TweetCreateView,
	TweetDetailView, 
	TweetListView,
	TweetUpdateView,
	TweetDeleteView
	)

urlpatterns = [
	url(r'^$', RedirectView.as_view(url="/")), # /tweet/
    url(r'^search/$', TweetListView.as_view(), name = 'list'), # /search/
    url(r'^create/$', TweetCreateView.as_view(), name = 'create'), # /tweet/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name = 'detail'), # /tweet/[number]/
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name = 'update'), # /tweet/[number]/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name = 'delete'), # /tweet/[number]/delete/
]