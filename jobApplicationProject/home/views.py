# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from controller.models import Position

# Create your views here.
def home (request):
    return render(request, 'home/home.html', {'home': 1})

def careers (request):
    openPositions = serializers.serialize( "python", Position.objects.filter(positionOpen = True) )
    return render(request, 'home/careers.html', {'openPositions': openPositions})