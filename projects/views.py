from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Projects,Image,Profile

# Create your views here.

def projects_today(request):
    date = dt.date.today()
    projects = Projects.today_projects()

    return render(request, 'today-projects.html',{"date":date,"projects":projects})   


def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = ""
        return render(request, 'search.html',{"message":message})


