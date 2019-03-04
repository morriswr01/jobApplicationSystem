from controller.models import *

def getUniversityInfofromStatus(status):
    universitityInfo = list()
    applications = Application.objects.filter(status = status)
    for application in applications:
        info = dict()
        appUni = Applications_Universities.objects.get(applicationID=application)
        info['degreeQualification'] = appUni.qualification
        info['degreeLevel'] = appUni.level
        info['universityAttended'] = appUni.universityID.name
        universitityInfo.append(info)
