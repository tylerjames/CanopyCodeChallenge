# Generated by Django 2.2.7 on 2019-11-06 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxoffice', '0003_fullschedule_theatreschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showing',
            old_name='ticketsSold',
            new_name='tickets_sold',
        ),
        migrations.AlterField(
            model_name='showing',
            name='timeslot',
            field=models.SmallIntegerField(),
        ),
    ]
