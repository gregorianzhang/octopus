from django.conf.urls import patterns, include, url
from containers import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='containers_list'),
    url(r'list/$', views.list, name='containers_list'),
    url(r'create/$', views.create, name='create'),
    url(r'destroy/(.+)/(http://.+)$', views.destroy, name='destroy'),
    url(r'detail/(.+)/(http://.+)$', views.detail, name='containers_detail'),
    url(r'start/(.+)/(http://.+)$', views.start, name='start'),
    url(r'stop/(.+)/(http://.+)$', views.stop, name='stop'),
    url(r'restart/(.+)/(http://.+)$', views.restart, name='restart'),
)
