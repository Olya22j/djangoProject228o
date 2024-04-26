from django.db import models

# Create your models here.
class ModelOla(models.Model):
    name = models.TextField()
    password = models.TextField()

class ModelOpa(models.Model):
    name1 = models.TextField()
    password1 = models.TextField()
