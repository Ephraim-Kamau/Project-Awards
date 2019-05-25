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
    
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

    )
    projects = models.ForeignKey(Projects, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)

    def __str__(self):
        return self.comment



