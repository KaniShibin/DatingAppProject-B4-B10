from django.db import models
from accounts.models import User
# Create your models here.
class UserPreference(models.Model):
    PREFFERED_GENDER_CHOICES=(('F','Female'),('M','Male'),('B','Both'))
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    preferred_gender = models.CharField(choices=PREFFERED_GENDER_CHOICES,max_length=1)
    prefered_age_min = models.CharField(max_length=50)
    prefered_age_max = models.CharField(max_length=50)
    location = models.ManyToManyField("userhome.Location")
    interests_hobbies = models.ManyToManyField("userhome.Interest")
    relationship = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    height_min = models.CharField(max_length=50)
    height_max = models.CharField(max_length=50)
    weight_min = models.CharField(max_length=50)
    weight_max = models.CharField(max_length=50)
    lifestyle = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)


class Location(models.Model):
    name = models.CharField(max_length=50)


class Interest(models.Model):
    name = models.CharField(max_length=50)