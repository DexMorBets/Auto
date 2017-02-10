from django.shortcuts import render

# coding=utf-8
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from .models import Service
from django.core.paginator import Paginator
from django.template.context_processors import csrf
from django.http import HttpResponse
# from .forms import
# from .models import


def mainpage(request):
    args = {}
    services = Service.objects.all()
    args['services'] = services
    return render(request, 'mainpage.html', args)