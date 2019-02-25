from django.db import models
import datetime

class User (models.Model):
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    salt  = models.CharField(max_length = 50)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 15)
    admin = models.BooleanField()
    hasApplied = models.BooleanField()

class Application (models.Model):
    completed =  models.BooleanField()
    dateSubmitted = models.DateField(auto_now_add= True)
    userID = models.ForeignKey(User,on_delete = models.CASCADE)

class Position (models.Model):
    positionName = models.CharField(max_length = 20)
    positionDescription = models.CharField(max_length = 50)
    openDate = models.DateField()
    deadlineDate = models.DateField()
    applicationID = models.ManyToManyField(Application, through = 'Applications_Positions')

class Applications_Positions (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    positionID = models.ForeignKey(Position, on_delete = models.CASCADE)
    feedback = models.CharField(max_length = 50)
    status = models.CharField (max_length = 10)

class ALevel (models.Model):
    subject = models.CharField(max_length = 30)
    applicationID = models.ManyToManyField(Application,through = 'Applications_ALevel')

class Applications_ALevel (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    alevelID = models.ForeignKey(ALevel, on_delete = models.CASCADE)
    grade = models.IntegerField()

class Language (models.Model):
    subject = models.CharField(max_length = 30)
    applicationID = models.ManyToManyField(Application, through = 'Applications_Languages')

class Applications_Languages (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    languageID = models.ForeignKey(Language, on_delete = models.CASCADE)
    expertise = models.IntegerField()

class Company (models.Model):
    companyName = models.CharField (max_length = 30)
    applicationID = models.ManyToManyField(Application,through = 'Applications_Employment')

class Applications_Employment (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    companyID = models.ForeignKey(Company, on_delete = models.CASCADE)
    position = models.CharField (max_length = 30)
    lengthOfEmployment = models.CharField (max_length = 30)

class University (models.Model):
    name = models.CharField(max_length = 50)
    applicationID = models.ManyToManyField(Application,through = 'Applications_Universities')

class Applications_Universities (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    universityID = models.ForeignKey(University, on_delete = models.CASCADE)
    qualification = models.CharField(max_length = 30)
    level = models.CharField(max_length = 30)

class Skill (models.Model):
    skillName = models.CharField(max_length = 30)
    applicationID = models.ManyToManyField (Application, through = 'Applications_Skills')

class Applications_Skills (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    skillID = models.ForeignKey(Skill, on_delete = models.CASCADE)
    expertise = models.IntegerField()

class Hobby (models.Model):
    name = models.CharField(max_length = 30)
    applicationID = models.ManyToManyField(Application,through = 'Applications_Hobbies')

class Applications_Hobbies (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    hobbyID = models.ForeignKey(Hobby, on_delete = models.CASCADE)
    interest = models.IntegerField()
