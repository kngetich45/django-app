import imp
from unicodedata import name
from urllib import request
from django import views
from django.test import RequestFactory, TestCase
from django.urls import reverse 
from . models import Member
from . views import frontend

# Create your tests here.
class ModelTesting(TestCase):
    
    def setUp(self):
        self.app = Member.objects.create(name='django',username='django',email='django',phone='django',age='django',location='django',gender='django',bio='django')


    def test_post_model(self):
        d = self.app
        self.assertTrue(isinstance(d, Member))
        self.assertEqual(str(d), 'django')
""" 
    def test_home_page_view(self):
        d = self.app
        url = reverse("App.views.frontend") 
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(d.name, resp.content)  """
