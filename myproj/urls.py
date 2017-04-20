# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.auth.views import login
from newsfeed.views import *
 
urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', login, name='login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
]