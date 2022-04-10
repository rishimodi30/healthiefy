import email
from pickle import TRUE
from typing_extensions import Required
from django.db import models

class Base_data(models.Model):
    
    p_name=models.CharField(max_length=30,default="",primary_key=True)
    p_email=models.EmailField(default="",primary_key=True)
    p_pwd = models.CharField(default="")
    
