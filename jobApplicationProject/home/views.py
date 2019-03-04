# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core import serializers
from controller.models import Positions

# Create your views here.
def home (request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'home/home.html', {'home': 1})

def careers (request):
    openPositions = serializers.serialize( "python", Positions.objects.filter(positionOpen = True) )
    # return redirect('dashboard')
    return render(request, 'home/careers.html', {'openPositions': openPositions})
