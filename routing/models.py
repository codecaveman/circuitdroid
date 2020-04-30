from django.db import models

from circuit.models import CircuitOverseer
from congregation.models import Congregation
# Create your models here.


class Week(models.Model):
    monday = models.DateField()
    congregation = models.ForeignKey(Congregation, on_delete=models.CASCADE)
    visiting_co = models.ForeignKey(CircuitOverseer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['monday']

    def __str__(self):
        return f'{self.monday} - {self.congregation}  - {self.visiting_co}'
