from django.db import models

# Create your models here.
class User_details(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    pass1=models.CharField(max_length=255)
    pass2=models.CharField(max_length=255)
