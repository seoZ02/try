from django.db import models

# Create your models here.
class First(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    part = models.CharField(max_length=20)
    demand = models.TextField(max_length=200)
    time = models.DateField()