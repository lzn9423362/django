from django.db import models

# Create your models here.



class User(models.Model):
    user = models.CharField(max_length=20)
    passwd = models.CharField(max_length=32)
    img = models.CharField(max_length=200)