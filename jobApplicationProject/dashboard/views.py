# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
    user = request.user
    if user.is_authenticated:
        if user.admin:
            return render(request, 'dashboard/admin.html')
        else:
            if user.hasApplied:
                return render(request, 'dashboard/applicant.html')
            else:
                return render(request, 'dashboard/createApplication.html')
    else: 
        return redirect('home-index')

def viewApplication(request):
    return render(request, 'dashboard/viewApplication.html')