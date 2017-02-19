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


class Price(models.Model):
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    title = models.CharField(verbose_name='Название', max_length=150)
    description = models.TextField(max_length=500, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    name = models.CharField(verbose_name='ФИО', max_length=150)
    position = models.TextField(max_length=500, verbose_name='Должность', null=True, blank=True)
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    phone_number2 = models.IntegerField(verbose_name='Номер телефона 2', null=True, blank=True)
    phone_number3 = models.IntegerField(verbose_name='Номер телефона 3', null=True, blank=True)
    photo = models.ImageField(upload_to='contacts/', blank=True)

    def __str__(self):
        return self.name