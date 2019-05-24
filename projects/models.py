from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    link_url = models.URLField(max_length=200)

class Profile(models.Model):
    bio = models.TextField(max_length=200)
    contact = models.IntegerField
    projects = models.ForeignKey(Projects)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
