from django.db import models


# Create your models here.
class Theatre(models.Model):
    seats = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=100)


class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    timeslot = models.IntegerField()
    ticketsSold = models.IntegerField()
    ticketsAvailable = models.IntegerField()
