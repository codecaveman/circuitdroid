from django.db import models

# Create your models here.


class Congregation(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.id) + ' - ' + self.name
