# Generated by Django 2.2 on 2020-04-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='type',
            field=models.CharField(choices=[('KMS', 'KMS'), ('PIO', 'PIO'), ('SCE', 'SCE'), ('SCOTW', 'SCOTW'), ('SKE', 'SKE')], max_length=20),
        ),
    ]
