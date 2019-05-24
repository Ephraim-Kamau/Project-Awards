from django.db import models
import datetime as dt

# Create your models here.
class Projects(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    link_url = models.URLField(max_length=200)
    projects_image = models.ImageField(upload_to = 'images/')

    @classmethod
    def today_projects(cls):
        today = dt.date.today()
        projects = cls.objects.filter()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects    

class Profile(models.Model):
    bio = models.TextField(max_length=200)
    contact = models.IntegerField(default=0, blank=True)
    projects = models.ForeignKey(Projects, null = True)
    profile_pic = models.ImageField(upload_to = 'images/')

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
