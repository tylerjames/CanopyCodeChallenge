# Generated by Django 2.2.7 on 2019-11-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxoffice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showing',
            name='ticketsAvailable',
        ),
        migrations.AlterField(
            model_name='showing',
            name='ticketsSold',
            field=models.IntegerField(default=0),
        ),
    ]