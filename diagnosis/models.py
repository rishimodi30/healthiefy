from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class MainData(models.Model):
    name= models.CharField(max_length=50,default="")
    city= models.CharField(max_length=50,default="")
    age=models.IntegerField(max_length=10,default=0)
    photo= models.ImageField(upload_to='pics',default=1)
    is_fat= models.BooleanField(default=False)

