#!/usr/bin/env python
from django.conf.urls import url
from .api import ListApi

app_name = 'historicRaces'
urlpatterns = [
    url(r'^fastlaps/$', ListApi.as_view()),
]