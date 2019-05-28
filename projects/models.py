from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length=200)
    contact = models.IntegerField(default=0, blank=True)
    profile_pic = models.ImageField(upload_to = 'images/')


class Projects(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    link_url = models.URLField(max_length=200)
    projects_image = models.ImageField(upload_to = 'images/')

    @classmethod
    def today_projects(cls):
        projects = cls.objects.filter()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects    

       

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    




