from controller.models import *
# returns an array of dictionaries, with fields fName and lName of the applicants
def getSubmittedApplicantName():
    nameArray = list()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        aux = dict()
        aux['fName'] = application.users.fName
        aux['lName'] = application.users.lName
        nameArray.append(aux)
    return nameArray
#returns a dictionary: key=applicationID and value the array of universities attended
def getSubmittedUniversityAttended():
    unisArray = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        universitiesList = list()
        universities = Applications_Universities.objects.filter(applicationID = application)
        for university in universities:
            universitiesList.append(university.universityID.name)
        unisArray[application.id] = universitiesList
    return unisArray
#returns a dictionary where key=applicationID, value= an array of Degree qualifications(in a specific order)
def getSubmittedDegreeQualification():
    degreesArray = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        degreeQualifList = list()
        universities = Applications_Universities.objects.filter(applicationID = application)
        for university in universities:
            degreeQualifList.append(university.qualification)
        degreesArray[application.id] = degreeQualifList
    return degreesArray
# return a dictionary, key = applicationID and value="Submitted" (No real reason for dict use honestly but...)
def getSubmittedApplications():
    appList = {}
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        appList[application.id] = "Submitted"

    return appList
#takes parameters applicationID = the ID of the application, and the new status, and updates the status in the database
def updateApplicationStatus(applicationID, newStatus):
    application = Application.objects.get(id = applicationID)
    application.status = newStatus
    application.save()

#Returns a dictionary with key=applicationID, value=tuple of (ALevel Name, ALevel Grade)
def getSubmittedALevels():
    ALevelsDict = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        ALevelList = list()
        ALevels = Applications_ALevels.objects.filter(applicationID = application)
        for ALevel in ALevels:
            ALevelList.append((ALevel.alevelID.subject,ALevel.grade))
        ALevelsDict[application.id] = ALevelList
    return ALevelsDict

#Returns a dictionary with key=applicationID, value = tuple of (Programming language name, Programming Language expertise)
def getSubmittedProgrammingLanguages():
    pLangsDict = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        pLangList = list()
        pLangs = Applications_Languages.objects.filter(applicationID = application)
        for pLang in pLangs:
            pLangList.append((pLang.languageID.subject,pLang.expertise))
        pLangsDict[application.id] = pLangList
    return pLangsDict

# returns a dictionary with key=applicationID
# the value is an array, with
# array[0] = name of the company
# array[1] = name of the position
# array[2] = length of Employment in months
def getSubmittedPreviousEmployment():
    employmentDict = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        employmentList = list()
        employments = Applications_Employments.objects.filter(applicationID = application)
        for employment in employments:
            employmentList.append([employment.companyID.companyName,employment.position,12*employment.lengthOfEmploymentYears+employment.lengthOfEmploymentMonths])
        employmentDict[application.id] = employmentList
    return employmentDict

# returns a dictionary with key = applicationID
# the value is an array, with
# array[0] = name of the skill
# array[1] = expertise
def getSubmittedSkills():
    skillsDict = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        skillsList = list()
        skills = Applications_Skills.objects.filter(applicationID = application)
        for skill in skills:
            skillsList.append([skill.skillID.skillName,skill.expertise])
        skillsDict[application.id] = skillsList
    return skillsDict


# returns a dictionary with key = applicationID
# the value is an array, with
# array[0] = name of the Hobby
# array[1] = interest
def getSubmittedHobbies():
    hobbiesDict = dict()
    applicationObj = Application.objects.filter(status='Submitted')
    for application in applicationObj:
        hobbiesList = list()
        hobbies = Applications_Hobbies.objects.filter(applicationID = application)
        for hobby in hobbies:
            hobbiesList.append([hobby.hobbyID.name,hobby.interest])
        hobbiesDict[application.id] = hobbiesList
    return hobbiesDict
