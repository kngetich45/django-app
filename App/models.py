from django.db import models

# Create your models here.
class Member(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', 'F')
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    location = models.CharField(max_length=3) 
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    bio = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
