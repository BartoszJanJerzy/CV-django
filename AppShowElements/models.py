from django.db import models

# Create your models here.

class Kurs(models.Model):
    title = models.TextField(max_length=256, unique=True)
    link = models.TextField(max_length=256,unique=True)
    icon = models.TextField(max_length=256, unique=False)
    icon2 = models.TextField(max_length=256, unique=False)

class Project(models.Model):
    title = models.TextField(max_length=256, unique=True)
    link = models.TextField(max_length=256,unique=True)
    icon = models.TextField(max_length=256, unique=False)