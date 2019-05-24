from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.projects_today,name='projectsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_projects,name = 'pastProjects'),
]