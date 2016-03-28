from django.conf.urls import patterns, include, url
from warfile import views

urlpatterns = patterns('',
    url(r'^$', views.lists, name='war_list'),
    url(r'lists/$', views.lists, name='war_lists'),
    url(r'upload/$', views.upload, name='war_upload'),
)
