#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Service, Price

admin.site.register(Service)
admin.site.register(Price)
