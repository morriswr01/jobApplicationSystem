# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home/home.html', {'home': 1})

def careers (request):
    return render(request, 'home/careers.html')