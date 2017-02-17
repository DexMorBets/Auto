#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^services/$', views.services_page, name='services_page'),
    url(r'^price/$', views.price_page, name='price_page'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^contacts/$', views.contacts_page, name='contacts_page'),
    url(r'^', views.mainpage, name='main_page'),
]