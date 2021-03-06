"""ask URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url

from qa import urls

urlpatterns = [
    url(r'^', include(urls)),
    url(r'^login/', include(urls)),
    url(r'^signup/.*', include(urls)),
    url(r'^question/(?P<id>[\d]+)/', include(urls)),
    url(r'^ask/.*', include(urls)),
    url(r'^popular/.*', include(urls)),
    url(r'^new/.*', include(urls)),
]
