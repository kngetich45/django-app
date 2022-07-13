from unicodedata import name
from django.test import TestCase
from . models import Member

# Create your tests here.
class ModelTesting(TestCase):
    
    def setUp(self):
        self.app = Member.objects.create(name='django',username='django',email='django',phone='django',age='django',location='django',gender='django',bio='django')


    def test_post_model(self):
        d = self.app
        self.assertTrue(isinstance(d, Member))