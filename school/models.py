from django.db import models

# Create your models here.


class School(models.Model):
    SchoolType = [
        ('KMS', 'KMS'),
        ('PIO', 'PIO'),
        ('SCE', 'SCE'),
        ('SCOTW', 'SCOTW'),
        ('SKE', 'SKE'),
    ]

    type = models.CharField(max_length=20, choices=SchoolType)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    a_instructor = models.CharField(max_length=80)

    def __str__(self):
        return self.type + ' - ' + str(self.start_date)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
