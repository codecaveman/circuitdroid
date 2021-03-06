# Generated by Django 2.2 on 2020-04-28 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_number', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('tuesday_service_talk', models.CharField(blank=True, max_length=255)),
                ('tuesday_song', models.CharField(blank=True, max_length=255)),
                ('public_talk', models.CharField(blank=True, max_length=255)),
                ('public_talk_song', models.CharField(blank=True, max_length=255)),
                ('concluding_talk', models.CharField(blank=True, max_length=255)),
                ('concluding_talk_song', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
