from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Projects,Image,Profile

# Create your views here.

def projects_today(request):
    date = dt.date.today()
    projects = Projects.today_projects()

    return render(request, 'all-projects/today-projects.html',{"date":date,"projects":projects})   

# View Function to present news from past days
def past_projects(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()  
        assert False  

    if date == dt.date.today():
        return redirect(projects_today)
    
    projects = Projects.today_projects()
    return render(request, 'all-projects/past-projects.html', {"date": date,"projects":projects}) 

def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"projects": searched_projects})

    else:
        message = ""
        return render(request, 'all-projects/search.html',{"message":message})


