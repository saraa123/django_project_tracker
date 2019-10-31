from django.db import models
from django.conf import settings 

# Create your models here.
class Item(models.Model):
    
    Issue = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.Issue
    
class Feature(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)


    def __str__(self):
        return self.name

