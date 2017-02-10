#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    title = models.CharField(verbose_name='Название услуги', max_length=100)
    description = models.TextField(max_length=400, verbose_name='Описание услуги')
    image = models.ImageField(upload_to='services/', blank=True)

    def __str__(self):
        return self.title
