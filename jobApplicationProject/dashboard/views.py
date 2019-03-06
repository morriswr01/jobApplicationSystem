# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import serializers
from django.shortcuts import render, redirect
from controller.models import *
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
def dashboard(request):
    user = request.user
    positionID = request.GET.get('pid')
    if user.is_authenticated:
        if user.admin:
            applications = getApplicants();
            return render(request, 'dashboard/admin/admin.html',{'applications':applications})
        else:
            if user.hasApplied:
                application = Application.objects.get(users = user)
                position = Application.objects.get(users = user).position
                return render(request, 'dashboard/applicant/applicant.html', {'application' : application, 'positionName':position.positionName})
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

def getApplicants():
    applicationDataObject = []
    applications = Application.objects.filter(Q(status = "Submitted")|Q(status = "Being Reviewed"))
    for applicant in applications:
        hobbies = Applications_Hobbies.objects.filter(applicationID = applicant)
        skills = Applications_Skills.objects.filter(applicationID = applicant)
        alevels = Applications_ALevels.objects.filter(applicationID = applicant)
        employments = Applications_Employments.objects.filter(applicationID = applicant)
        university = Applications_Universities.objects.get(applicationID = applicant)
        languages = Applications_Languages.objects.filter(applicationID = applicant)
        applicationDataObject.append({'applicant':applicant,'skills':skills,'hobbies':hobbies,'aLevels':alevels,'employments':employments,'university':university,'languages':languages})
    return applicationDataObject

def adminPositions(request):
    positions = serializers.serialize( "python", Positions.objects.all())
    return render(request, 'dashboard/admin/editPositions.html', {'positions': positions})

def adminFeedback(request):
    applicationsInterviewed = Application.objects.filter(Q(status = "Interviewed"))
    applicationsInterviewRequest = Application.objects.filter(Q(status = "Requested Interview"))
    applicationsAccepted = Application.objects.filter(Q(status = "Accepted"))
    return render(request, 'dashboard/admin/feedback.html', {'applicationsInterviewRequest':applicationsInterviewRequest, 'applicationsInterviewed': applicationsInterviewed, 'applicationsAccepted': applicationsAccepted })

def addNewPosition(request):
    jobTitle = request.POST.get('jobTitle')
    deadlineDate = request.POST.get('deadline')
    jobDescription = request.POST.get('jobDescription')
    newJob = Positions(positionName = jobTitle, positionDescription = jobDescription,deadlineDate= deadlineDate)
    newJob.save()
    return redirect('adminPositions')

def editPosition(request):
    positionID = request.POST.get('positionID')
    position = Positions.objects.get(id = positionID)
    jobTitle = request.POST.get('newJobTitle')
    deadlineDate = request.POST.get('newDeadline')
    jobDescription = request.POST.get('newJobDescription')
    position.positionName = jobTitle
    position.deadlineDate = deadlineDate
    position.positionDescription = jobDescription
    position.save()
    return redirect('adminPositions')

def deletePosition(request):
    positionID=request.POST.get('positionID')
    data = dict()
    Positions.objects.filter(id=positionID).delete()
    return JsonResponse(data)

@csrf_exempt
def rejectWithFeedback(request):
        data = dict()
        applicationID = request.POST.get('appId')
        feedback = request.POST.get('feedback')
        application = Application.objects.get(id = applicationID)
        application.status = Application.rejected
        application.feedback = feedback
        application.save()
        return redirect('adminFeedback')
        
@csrf_exempt
def hireApplicant(request):
        data = dict()
        applicationID = request.GET.get('appId')
        application = Application.objects.get(id = applicationID)
        application.status = Application.accepted
        application.save()
        return redirect('adminFeedback')

def viewApplication(request):
    application = Application.objects.get(users=request.user)
    hobbies = Applications_Hobbies.objects.filter(applicationID = application)
    skills = Applications_Skills.objects.filter(applicationID = application)
    alevels = Applications_ALevels.objects.filter(applicationID = application)
    employments = Applications_Employments.objects.filter(applicationID = application)
    university = Applications_Universities.objects.get(applicationID = application)
    languages = Applications_Languages.objects.filter(applicationID = application)
    return render(request, 'dashboard/applicant/viewApplication.html',{'application':application,'skills':skills,'hobbies':hobbies,'aLevels':alevels,'employments':employments,'university':university,'languages':languages, 'home': 1})

@csrf_exempt
def adminAction(request):
    data = dict()
    applicationID = request.POST.get('applicationID')
    action = request.POST.get('action')
    application = Application.objects.get(id = applicationID)
    if action == "requestInterview":
        application.status = Application.interviewRequest
        application.save()
    elif action == "rejectApplicant":
        application.status = Application.rejected
        application.save()
    return JsonResponse(data)

@csrf_exempt
def rejectInterview(request):
    applicationID = request.GET.get('appId')
    application = Application.objects.get(id = applicationID)
    application.status = Application.rejected
    application.save()
    return redirect('dashboard')


@csrf_exempt
def acceptInterview(request):
    applicationID = request.GET.get('appId')
    application = Application.objects.get(id = applicationID)
    application.status = Application.interviewed
    application.save()
    return redirect('dashboard')
