from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    
class Block(models.Model):
    SUBJECT_CHOICES = (
        ("Art", "Art"),
        ("English", "English"),
        ("History", "History"),
        ("Math", "Math"),
        ("Science", "Science"),
        ("World Language", "World Language"),
        ("Elective", "Elective"),
    )
    
    user = models.ForeignKey(User, related_name="blocks")
    
    start_timestamp = models.IntegerField()
    end_timestamp = models.IntegerField()
    
    subject = models.CharField(max_length=15, choices=SUBJECT_CHOICES)