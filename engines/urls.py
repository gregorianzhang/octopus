from django.conf.urls import patterns, include, url
from engines import views

urlpatterns = patterns('',
    url(r'^$', views.lists, name='lists'),
    url(r'lists/$', views.lists, name='lists'),
    url(r'add/$', views.add, name='add'),
    url(r'remove/$', views.remove, name='remove'),
    url(r'detail/(http://.+)$', views.detail, name='detail'),
)
