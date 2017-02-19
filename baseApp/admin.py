#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Service, Price, Contact

admin.site.register(Service)
admin.site.register(Price)
admin.site.register(Contact)
