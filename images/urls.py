from django.conf.urls import patterns, include, url
from engines import views

urlpatterns = patterns('',
    url(r'^$', views.lists, name='images_lists'),
    url(r'lists/$', views.lists, name='images_lists'),
)
