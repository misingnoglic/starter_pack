__author__ = 'arya'
from django.conf.urls import patterns, url

from generate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)