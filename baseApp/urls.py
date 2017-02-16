#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^services/$', views.services_page, name='services_page'),
    url(r'^', views.mainpage, name='main_page'),
]