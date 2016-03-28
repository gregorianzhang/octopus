"""octopus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from engines import urls as engines_urls
from containers import urls as containers_urls
from images import urls as images_urls
from warfile import urls as warfile_urls
from account import urls as account_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^engines/', include(engines_urls)),
    url(r'^containers/', include(containers_urls)),
    url(r'^images/', include(images_urls)),
    url(r'^warfile/', include(warfile_urls)),
    url(r'^account/', include(account_urls)),
    
]
