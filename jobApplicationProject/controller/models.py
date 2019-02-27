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

class Positions (models.Model):
    positionName = models.CharField(max_length = 20)
    positionDescription = models.TextField()
    positionOpen = models.BooleanField(default=False)
    deadlineDate = models.DateField()

class Application(models.Model):
    completed =  models.BooleanField()
    dateSubmitted = models.DateField(auto_now_add= True)
    submitted = 'submitted'
    interview = 'interview'
    rejected = 'rejected'
    accepted = 'accepted'
    statusChoices = (
        (submitted, 'Submitted'),
        (interview, 'Interview'),
        (rejected, 'Rejected'),
        (accepted, 'Accepted')
    )
    status = models.CharField(
        max_length = 10,
        choices = statusChoices,
        default = 'submitted',   
    )
    feedback = models.CharField(max_length = 50)
    userID = models.OneToOneField(User, on_delete = models.DO_NOTHING)
    positionID = models.OneToOneField(Positions, on_delete = models.DO_NOTHING)

class PreviousEmployment(models.Model):
    companyName = models.CharField(max_length = 30)
    jobTitle = models.CharField(max_length = 30)
    lengthOfEmployment = models.DurationField()
    applicationID = models.ForeignKey(Application, on_delete = models.DO_NOTHING)

class Degree(models.Model):
    degreeTitle = models.CharField(max_length = 50)
    degreeGrade = models.CharField(max_length = 50)
    degreeType = models.CharField(max_length = 50)
    universityName = models.CharField(max_length = 50)
    applicationID = models.ForeignKey(Application, on_delete = models.DO_NOTHING)

class ALevels(models.Model):
    subject = models.CharField(max_length = 30)
    grade = models.CharField(max_length = 2)
    applicationID = models.ForeignKey(Application, on_delete = models.DO_NOTHING)

class ProgrammingLanguages(models.Model):
    name = models.CharField(max_length = 30)
    proficiency = models.IntegerField()
    applicationID = models.ForeignKey(Application, on_delete = models.DO_NOTHING)

class Skills(models.Model):
    name = models.CharField(max_length = 30)
    expertise = models.IntegerField()
    applicationID = models.ForeignKey(Application, on_delete = models.DO_NOTHING)

class Hobbies(models.Model):
    name = models.CharField(max_length = 30)
    expertise = models.IntegerField()
    applicationID = models.ForeignKey(Application, on_delete = models.DO_NOTHING)
