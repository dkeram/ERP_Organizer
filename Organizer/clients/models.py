from django.db import models

# Create your models here.


class Clients(models.Model):
    sirname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    vat = models.IntegerField(unique=True)
    phone = models.IntegerField(blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    user_name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
