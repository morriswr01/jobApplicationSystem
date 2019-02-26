from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import datetime


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, fName, lName, admin, hasApplied, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        if not fName:
            raise ValueError('The First Name must be set')
        if not lName:
            raise ValueError('The Last Name must be set')

        user = self.model(
            email = self.normalize_email(email),
            fName = fName,
            lName = lName,
            admin = admin,
            hasApplied = hasApplied,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, fName, lName, admin, hasApplied, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, fName, lName, admin, hasApplied, **extra_fields)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    fName = models.CharField(max_length = 15)
    lName = models.CharField(max_length = 15)
    admin = models.BooleanField(default=False)
    hasApplied = models.BooleanField(default=False)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    REQUIRED_FIELDS = ['fName', 'lName', 'admin', 'hasApplied']
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

class Application (models.Model):
    completed =  models.BooleanField()
    dateSubmitted = models.DateField(auto_now_add= True)
    userID = models.ForeignKey(User, on_delete = models.CASCADE)

class Position (models.Model):
    positionName = models.CharField(max_length = 20)
    positionDescription = models.CharField(max_length = 50)
    positionOpen = models.BooleanField(default=False)
    deadlineDate = models.DateField()
    applicationID = models.ManyToManyField(Application, through = 'Applications_Positions')

class Applications_Positions (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    positionID = models.ForeignKey(Position, on_delete = models.CASCADE)
    feedback = models.CharField(max_length = 50)
    status = models.CharField (max_length = 10)

class ALevel (models.Model):
    applicationID = models.ManyToManyField(Application,through = 'Applications_ALevel')
    subject = models.CharField(max_length = 30)

class Applications_ALevel (models.Model):
    applicationID = models.ForeignKey(Application, on_delete = models.CASCADE)
    alevelID = models.ForeignKey(ALevel, on_delete = models.CASCADE)
    grade = models.IntegerField()

class Language (models.Model):
    applicationID = models.ManyToManyField(Application, through = 'Applications_Languages')
    subject = models.CharField(max_length = 30)

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

