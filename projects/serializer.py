from rest_framework import serializers
from .models import Projects,Profile

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'link_url')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'contact')        


  