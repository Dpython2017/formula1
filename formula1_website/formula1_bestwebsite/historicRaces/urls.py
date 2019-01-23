#!/usr/bin/env python
from django.conf.urls import url
from .api import ListApi,DetailApi,LapUpdateApi,LapRetrieve,LapDestroy

app_name = 'historicRaces'
urlpatterns = [
    url(r'^fastlaps/$', ListApi.as_view()),
    url(r'^detail/$',DetailApi.as_view()),
    url(r'^lap/(?P<pk>\d+)/update$', LapUpdateApi.as_view()),
    url(r'^lap/(?P<pk>\d+)$', LapRetrieve.as_view()),
    url(r'^lap/(?P<pk>\d+)/delete$', LapDestroy.as_view()),
]