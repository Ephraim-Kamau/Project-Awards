from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import NewProfileForm,NewProjectsForm
from .models import Projects,Image,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def projects_today(request):
    projects = Projects.objects.all()

    return render(request, 'today-projects.html', {"projects":projects})   

def profile(request):

    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')    
def new_profile(request):
    current_user=request.user

    if request.method=='POST':
        form=NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("profile")
    else:
        form = NewProfileForm() 
    return render(request,'upload.html',{"form":form}) 

@login_required(login_url='/accounts/login/')    
def new_project(request):
    current_user=request.user

    if request.method=='POST':
        form=NewProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("today-projects")
    else:
        form = NewProjectsForm() 
    return render(request,'project.html',{"form":form})     

def search_results(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = ""
        return render(request, 'search.html',{"message":message})


