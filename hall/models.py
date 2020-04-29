from django.db import models

# Create your models here.


class Hall(models.Model):
    number = models.CharField(max_length=5)
    road = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=15)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.road


class Sharing(models.Model):
    name = models.CharField(max_length=255)
