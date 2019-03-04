# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from controller.models import Application

# Create your views here.
def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if user.admin:
            return render(request, 'dashboard/admin.html')
        else:
            if user.hasApplied:
                application = Application.objects.get(users = user)
                return render(request, 'dashboard/applicant.html', {'application': application})
            else:
                return render(request, 'dashboard/createApplication.html')
    else: 
        return redirect('home-index')

def viewApplication(request):
    user = request.user
    application = Application.objects.get(users = user)
    return render(request, 'dashboard/viewApplication.html', {'application': application})