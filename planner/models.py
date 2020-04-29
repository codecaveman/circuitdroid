from django.db import models

# Create your models here.


class Week(models.Model):
    week = models.CharField(max_length=100)

    def __str__(self):
        return self.week
