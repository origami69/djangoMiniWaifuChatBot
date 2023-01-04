from django.db import models

# Create your models here.
from django.db import models


class userDat(models.Model):
    user_name = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

class Person(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)

