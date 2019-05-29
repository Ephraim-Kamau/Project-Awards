from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.projects_today,name='projectsToday'),
    url(r'^search/', views.search_results, name='search_results'),   
    url(r'^profile/', views.profile, name='profile'), 
    url(r'new/profile$',views.new_profile,name='new_profile'),
    url(r'^new/project$',views.new_project,name='new_project'),
    url(r'^find_project/(\d+)',views.find_project,name = 'find_project'),
    url(r'^api/projects/$', views.Projecti.as_view()),
    url(r'^api/profile/$', views.Profile.as_view())



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)