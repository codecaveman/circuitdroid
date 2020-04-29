from django.db import models

# Create your models here.


class Meeting(models.Model):
    VisitNumber = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    ]

    visit_number = models.IntegerField(choices=VisitNumber)
    tuesday_service_talk = models.CharField(max_length=255, blank=True)
    tuesday_song = models.CharField(max_length=255, blank=True)
    public_talk = models.CharField(max_length=255, blank=True)
    public_talk_song = models.CharField(max_length=255, blank=True)
    concluding_talk = models.CharField(max_length=255, blank=True)
    concluding_talk_song = models.CharField(max_length=255, blank=True)
