from django.db import models
from circuit.models import Congregation
# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50, blank=True)
    congregation = models.ForeignKey(Congregation, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

