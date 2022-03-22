from django.db import models

class users(models.Model):
    username=models.CharField(max_length=10)
    paswword=models.CharField(max_length=10)
    fullname=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    age=models.IntegerField()

