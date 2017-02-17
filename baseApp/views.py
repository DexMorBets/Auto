from django.shortcuts import render

# coding=utf-8
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from .models import Service, Price
from django.core.paginator import Paginator
from django.template.context_processors import csrf
from django.http import HttpResponse
# from .forms import
# from .models import


def mainpage(request):
    args = {}
    services = Service.objects.all()[:3]
    args['services'] = services
    return render(request, 'mainpage.html', args)


def services_page(request):
    args = {}
    services = Service.objects.all()
    args['services'] = services
    return render(request, 'services_page.html', args)


def price_page(request):
    args = {}
    prices = Price.objects.all()
    args["prices"] = prices
    return render(request, 'price_page.html', args)


def about_page(request):
    args = {}
    return render(request, 'about_page.html', args)


def contacts_page(request):
    args = {}
    return render(request, 'contact_page.html', args)