from django.test import TestCase
from .models import Projects,Profile

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.ephraim = Profile(id = 125, profile_pic = "",bio = "I love fast cars and planes")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ephraim,Profile))
    
    def test_initialization(self):
        self.assertEqual(self.ephraim.profile_pic,"")
        self.assertEqual(self.ephraim.bio, "I love fast cars and planes")

    # Testing Save method
    def test_save(self):
        self.ephraim.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    # Testing Delete method
    def test_delete(self):
        self.ephraim.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ProjectsTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Profile class test
        self.ephraim = Profile( bio = "I love fast cars and planes")

        # Project class Test
        self.project = Projects(title = "Instagram", projects_image = " ",description="Digi Digi",link_url = "")
        self.project.save_project()


    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Projects))

    # Testing Save method
    def test_save_method(self):
        self.project.save_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.project.delete_project()
        projects = Projects.objects.all()
        self.assertTrue(len(projects) == 0)


