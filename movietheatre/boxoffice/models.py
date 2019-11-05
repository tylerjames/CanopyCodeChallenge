from django.db import models


# Create your models here.
class Theatre(models.Model):
    seats = models.IntegerField()

    def __str__(self):
        return f'Theatre ({self.id}) with {self.seats} seats'


class Movie(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TheatreSchedule(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    showings = models.ManyToManyField(Showing)


class FullSchedule(models.Model):
    theatreSchedules = models.ManyToManyField(TheatreSchedule)


class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    timeslot = models.IntegerField()
    ticketsSold = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.movie.title} in theatre {self.theatre.id} at timeslot {self.timeslot}'

    def ticketsRemaining(self):
        return self.theatre.seats - self.ticketsSold

    def issueTickets(self, count):
        if self.ticketsRemaining() < count:
            return "Not enough seats remaining"
        self.ticketsSold += count
        return "Tickets issued"

    def revokeTickets(self, count):
        if (self.ticketsRemaining() + count) > self.theatre.seats:
            return "Trying to revoke more tickets than there are seats"
        self.ticketsSold -= count
