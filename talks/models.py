from django.db import models

# Create your models here.


class Talk(models.Model):

    Tuesday = 'Tue'
    Pioneer = 'Pio'
    EldersAndServants = 'E&MS'
    PublicTalk = 'PT'
    FinalTalk = 'FT'
    TalkTypes = [
        (Tuesday, 'Tuesday Service Talk'),
        (Pioneer, 'Pioneer Meeting'),
        (EldersAndServants, 'Elders and Servants'),
        (PublicTalk, 'Public Talk'),
        (FinalTalk, 'Concluding Service Talk'),
    ]

    talk_type = models.CharField(
        max_length=20,
        choices=TalkTypes
    )

    VistNumber = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    ]

    visit_number = models.IntegerField(choices=VistNumber)
    title = models.CharField(max_length=100)
    song = models.CharField(max_length=200)

    def __str__(self):
        return self.talk_type
