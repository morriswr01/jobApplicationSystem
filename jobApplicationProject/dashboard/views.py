# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.shortcuts import render, redirect
from controller.models import *
from django.db.models import Q

# Create your views here.
def dashboard(request):
    user = request.user
    positionID = request.GET.get('pid')
    if user.is_authenticated:
        if user.admin:
            applications = Application.objects.filter(Q(status = "Submitted")|Q(status = "Being Reviewed"))

            return render(request, 'dashboard/admin/admin.html',{'applications':applications})
        else:
            if user.hasApplied:
                applicationStatus = Application.objects.get(users=user).status
                position = Application.objects.get(users = user).position
                return render(request, 'dashboard/applicant/applicant.html', {'applicationStatus' : applicationStatus, 'positionName':position.positionName})
            else:
                if positionID is not None:
                    return render(request, 'dashboard/applicant/createApplication.html', {'positionID': positionID})
                else:
                    openPositions = serializers.serialize( "python", Positions.objects.filter(positionOpen = True) )
                    return render(request, 'home/careers.html', {'openPositions': openPositions})
    else:
        if positionID is not None:
            return render(request, 'controller/signUp.html', {'positionID': positionID})
        else:
            openPositions = serializers.serialize( "python", Positions.objects.filter(positionOpen = True) )
            return render(request, 'home/careers.html', {'openPositions': openPositions})

def adminPositions(request):
    positions = serializers.serialize( "python", Positions.objects.all())
    return render(request, 'dashboard/admin/editPositions.html', {'positions': positions})

def adminFeedback(request):
    return render(request, 'dashboard/admin/feedback.html')

def viewApplication(request):
    applicationObject = Application.objects.get(users=request.user)
    hobbiesObject = Applications_Hobbies.objects.filter(applicationID = applicationObject)
    skillsObject = Applications_Skills.objects.filter(applicationID = applicationObject)
    alevelsObject = Applications_ALevels.objects.filter(applicationID = applicationObject)
    employmentsObject = Applications_Employments.objects.filter(applicationID = applicationObject)
    universitiesObject = Applications_Universities.objects.filter(applicationID = applicationObject)
    languagesObject = Applications_Languages.objects.filter(applicationID = applicationObject)
    return render(request, 'dashboard/applicant/viewApplication.html',{'applicationObject':applicationObject,'skillsObject':skillsObject,'hobbiesObject':hobbiesObject,'aLevelsObject':alevelsObject,'employmentsObject':employmentsObject,'universitiesObject':universitiesObject,'languagesObject':languagesObject})
