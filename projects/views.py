from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .forms import NewProfileForm,NewProjectsForm
from .models import Projects,Image,Profile
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectsSerializer,ProfileSerializer

# Create your views here.

@login_required(login_url='/accounts/login/')
def projects_today(request):
    projects = Projects.objects.all()

    return render(request, 'today-projects.html', {"projects":projects})   

def profile(request):
    current_user=request.user
    projects = Projects.objects.filter(profile = current_user)


    return render(request, 'profile.html', {"projects":projects,"current_user":current_user, "prrofile":profile})

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
        return redirect('projectsToday')
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
        message = "You haven't searched for any projects!!"
        return render(request, 'search.html',{"message":message})

def find_project(request,project_id):
    project_id
    try :
        project = Project.objects.get(user_id = project_id)

    except ObjectDoesNotExist:
        
        raise Http404()

    return render(request, 'find_project.html', {"project":project, "project_id":project_id})

class Projects(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = Project(all_projects, many=True)
        return Response(serializers.data)

class Profile(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = Profile(all_profile, many=True)
        return Response(serializers.data)
