# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from controller.models import *

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

def changePassword(request):
    currentPassword = request.POST['password']
    newPassword = request.POST['new-password']
    confirmPassword = request.POST['confirm-new-password']
    if newPassword == confirmPassword and request.user.check_password(currentPassword):
        user = User.objects.get(id = request.user.id)
        user.set_password(newPassword)
        user.save()
        return redirect('dashboard')
    return redirect('home')
def submitApp(request):
    user = request.user
    degreeType = request.POST['degreeType']
    degreeTitle = request.POST['degreeTitle']
    degreeGrade = request.POST['degreeGrade']
    universityAttended = request.POST.get('universityAttended')
    alevelsName = request.POST.getlist("a-levels[name]")
    alevelsProficiency = request.POST.getlist('a-levels[proficiency]')
    companyName = request.POST.getlist('previousEmployment[companyName]')
    postName = request.POST.getlist('previousEmployment[postName]')
    yearsLength = request.POST.getlist('previousEmployment[lengthYears]')
    monthsLength = request.POST.getlist('previousEmployment[lengthMonths]')
    progLangName = request.POST.getlist('progLanguages[name]')
    progLangproficiency = request.POST.getlist('progLanguages[proficiency]')
    skillsName = request.POST.getlist('skills[name]')
    skillProficiency = request.POST.getlist('skills[proficiency]')
    hobbiesName = request.POST.getlist('hobbies[name]')
    hobbyProficiency = request.POST.getlist('hobbies[proficiency]')
    print("PIZDA MASII")
    positionID = request.GET.get('pid')
    print(positionID)
    position = Positions.objects.get(id = positionID)
    applicationObj = Application.objects.create(completed = 1,feedback = '',users = user,position = position)
    applicationObj.save()
    applicationID = applicationObj.id
    user = User.objects.get(id = request.user.id)
    user.hasApplied = True
    user.save()
    ############### DEGREE AND UNIVERSITIES ATTENDED ##############
    addUniDetails (applicationObj,applicationID,universityAttended,degreeTitle,degreeGrade)
    ############### A LEVELS ##############
    addALevelDetails (applicationObj,applicationID,alevelsName,alevelsProficiency)
    ############### PREVIOUS EMPLOYMENT ##############
    addpreviousEmploymentDetails (applicationObj,applicationID,companyName,postName,yearsLength,monthsLength)
    ################ PROGRAMMING LANGUAGES ############
    addProgrammingLanguagesDetails (applicationObj,applicationID,progLangName,progLangproficiency)
    ################  SKILLS  ##############
    addSkillsDetails(applicationObj,applicationID,skillsName,skillProficiency)

    ################ HOBBIES ###############
    addHobbiesDetails (applicationObj,applicationID,hobbiesName,hobbyProficiency)



    return redirect('dashboard')

def addALevelDetails (applicationObj,applicationID,alevelsName,alevelsProficiency):
    for i in range(len(alevelsName)):
        ALevelObj,created = ALevels.objects.get_or_create(subject = alevelsName[i])
        alevels_appsObj = Applications_ALevels(applicationID=applicationObj,alevelID=ALevelObj,grade = alevelsProficiency[i])
        alevels_appsObj.save()
def addUniDetails (applicationObj,applicationID,universityAttended,degreeTitle,degreeGrade):
    universityObj,created = Universities.objects.get_or_create(name = universityAttended)
    uni_appsObj = Applications_Universities.objects.create(applicationID = applicationObj,universityID = universityObj,qualification = degreeTitle,level = degreeGrade )
    uni_appsObj.save()

def addpreviousEmploymentDetails (applicationObj,applicationID,companyName,postName,yearsLength,monthsLength):
    for i in range(len(companyName)):
        companyObj,created= Companies.objects.get_or_create(companyName = companyName[i])
        app_employmentsObj = Applications_Employments(applicationID=applicationObj,companyID=companyObj,position = postName[i],lengthOfEmploymentYears = yearsLength[i],lengthOfEmploymentMonths = monthsLength[i])
        app_employmentsObj.save()
def addProgrammingLanguagesDetails (applicationObj,applicationID,progLangName,progLangproficiency):
    for i in range(len(progLangName)):
        programmingLanguagesObj,created = Languages.objects.get_or_create(subject = progLangName[i])
        languages_AppsObj = Applications_Languages(applicationID=applicationObj,languageID=programmingLanguagesObj,expertise =progLangproficiency[i])
        languages_AppsObj.save()

def addSkillsDetails (applicationObj,applicationID,skillsName,skillProficiency):
    for i in range(len(skillsName)):
        skillObj,created = Skills.objects.get_or_create(skillName = skillsName[i])
        skills_AppsObj = Applications_Skills(applicationID=applicationObj,skillID=skillObj,expertise = skillProficiency[i])
        skills_AppsObj.save()
def addHobbiesDetails (applicationObj,applicationID,hobbiesName,hobbyProficiency):
    for i in range(len(hobbiesName)):
        hobbyObj,created = Hobbies.objects.get_or_create(name = hobbiesName[i])
        hobbies_AppsObj = Applications_Hobbies(applicationID=applicationObj,hobbyID=hobbyObj,interest = hobbyProficiency[i])
        hobbies_AppsObj.save()
def addNewSkill (skillName):
    newSkill = Skills(skillName = skillName)
    newSkill.save()
