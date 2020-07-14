""" URL Configuration

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
from django.conf.urls.static import static

import lib.csrftokengen
import lib.common
import os

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/getcsrftoken', lib.csrftokengen.getToken),
    url(r'^api/mgr/', include('apps.mgr.urls')),
    url(r'^apijson/mgr/', include('apps.mgr.urls')),
    url(r'^apixml/mgr/', include('apps.mgr.urls')),
    url(r'^api/teacher/', include('apps.teacher.urls')),
    url(r'^api/student/', include('apps.student.urls'))
]  \
    + static("/", document_root="../static")


