# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserSignUpForm

def signUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'controller/signUp.html', {'duplicateEmail': True})
    return render(request, 'controller/signup.html')

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'home/home.html', {'errors': True})
    return render(request, 'home/home.html')

def logoutUser(request):
    logout(request)
    return redirect('home-index')