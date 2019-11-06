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


class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    timeslot = models.SmallIntegerField()
    tickets_sold = models.IntegerField(default=0)

    show_times = ['8:00am-10:00am', '10:00am-12:00pm', '12:00pm-2:00pm',
                  '2:00pm-4:00pm', '4:00pm-6:00pm', '8:00pm-10:00pm', '10:00pm-12:00am']

    @property
    def show_time(self):
        print(f"Timeslot: {self.timeslot}")
        if self.timeslot < 0 or self.timeslot >= len(self.show_times):
            return "Invalid timeslot"
        return self.show_times[self.timeslot]

    @property
    def seats_remaining(self):
        return self.theatre.seats - self.tickets_sold

    def issue_tickets(self, count):
        if self.seats_remaining < count:
            return "Not enough seats remaining"
        self.tickets_sold += count
        return "Tickets issued"

    def revoke_tickets(self, count):
        if count > self.tickets_sold:
            return "Error: Trying to revoke more tickets than were sold"
        if (self.seats_remaining + count) > self.theatre.seats:
            return "Error: Trying to revoke more tickets than there are seats"
        self.tickets_sold -= count

    def __str__(self):
        return f'{self.movie.title} in theatre {self.theatre.id} at timeslot {self.timeslot}'
