from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    bio = models.TextField(max_length=200)
    contact = models.IntegerField(default=0, blank=True)
    profile_pic = models.ImageField(upload_to = 'images/')


    @classmethod
    def get_projects(cls):
        projects= Projects.objects.all()
        return projects 

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()  
      


class Projects(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    link_url = models.URLField(max_length=200)
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    projects_image = models.ImageField(upload_to = 'images/')
    
    class Meta:
        verbose_name='Project'
        verbose_name_plural='Projects'

    @classmethod
    def today_projects(cls):
        projects = cls.objects.filter()
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects  

    @classmethod
    def get_projects(cls):
        projects= Projects.objects.all()
        return projects 

    def save_project(self):
        self.save() 

    def delete_project(self):
        self.delete()     

       

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def save_image(self):
        self.save()

       


