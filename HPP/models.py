from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PersonalUser(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=250,blank=True, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

class HousingData(models.Model):
    area = models.CharField(max_length=250, null=True, blank=True)
    base_area = models.CharField(max_length=250, null=True, blank=True)
    bedrooms = models.CharField(max_length=250, null=True, blank=True)
    bathrooms = models.CharField(max_length=250, null=True, blank=True)
    stories = models.CharField(max_length=250, null=True, blank=True)
    guestroom = models.CharField(max_length=250, null=True, blank=True)
    parking = models.CharField(max_length=250, null=True, blank=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    

class Plan(models.Model):
    area_category = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.area_category

class PostImage(models.Model):
    plan = models.ForeignKey(Plan, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.plan.area_category