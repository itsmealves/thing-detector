# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render('index')

def not_found(request):
    return redirect('/')
