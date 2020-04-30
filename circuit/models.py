from django.db import models

# Create your models here.


class CircuitOverseer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Circuit(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CircuitSection(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class KingdomHall(models.Model):
    number = models.CharField(max_length=30)
    road = models.CharField(max_length=300)
    postcode = models.CharField(max_length=30)
    telephone = models.CharField(max_length=20)
    wifi = models.CharField(max_length=50)

    def __str__(self):
        return self.road


class Congregation(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    # circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    # address = models.ForeignKey(KingdomHall, on_delete=models.CASCADE)
    # circuit_section = models.ForeignKey(
    #     CircuitSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
