# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index (request):
    # return HttpResponse('Hello From Home')
    return render(request, 'createApplication/index.html', {'home': 0})