from django.db import models
import django.db.backends.mysql
# Create your models here.

class student(models.Model):
   fnam=models.CharField(max_length=50)
   id=models.IntegerField(unique=True),
   address=models.CharField(max_length=50)