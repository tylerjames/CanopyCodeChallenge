from django.test import TestCase

from movietheatre.boxoffice.models import Movie, Showing, Theatre


# Create your tests here.
class ShowingTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="Shawshank Redemption")
        Theatre.objects.create(seats=50)

    def test_can_create(self):
        """
        Tests showing creation and basic assignments
                """
        movie = Movie.objects.first()
        theatre = Theatre.objects.first()

        showing = Showing(movie=movie, theatre=theatre, timeslot=4)

        # Make sure the movie was properly assigned
        self.assertEqual(showing.movie.id, movie.id)

        # Make sure the theatre was properly assigned
        self.assertEqual(showing.theatre.id, theatre.id)

        # Make sure the timeslot was properly assigned
        self.assertEqual(showing.timeslot, 4)

    def test_issuing_tickets_decrements_seats(self):
        movie = Movie.objects.first()
        theatre = Theatre.objects.first()

        showing = Showing(movie=movie, theatre=theatre, timeslot=4)

        # Theatre was made with 50 seats
        showing.issue_tickets(10)

        self.assertEqual(showing.seats_remaining, 40)

    def test_issuing_too_many_tickets_fails(self):
        movie = Movie.objects.first()
        theatre = Theatre.objects.first()

        showing = Showing(movie=movie, theatre=theatre, timeslot=4)

        # Theatre was made with 50 seats
        showing.issue_tickets(100)

        # Should still have 50 seats if 100 seat purchase was rejected
        self.assertEqual(showing.seats_remaining, 50)

    def test_revoking_tickets_increments_seats_available(self):
        """
        Revoking tickets (refunding) should increase the number of seats available predictably
                """
        movie = Movie.objects.first()
        theatre = Theatre.objects.first()

        showing = Showing(movie=movie, theatre=theatre, timeslot=4)

        # Issue 20 tickets
        showing.issue_tickets(20)

        # Revoke 15 tickets
        showing.revoke_tickets(15)

        # Seats remaining should be 50 - 20 + 15 = 45
        self.assertEqual(showing.seats_remaining, 45)

    def test_revoking_too_many_tickets_fails(self):
        """
        Should not be able to revoke more tickets than were issued
        """
        movie = Movie.objects.first()
        theatre = Theatre.objects.first()

        showing = Showing(movie=movie, theatre=theatre, timeslot=4)

        # Issue 10 tickets
        showing.issue_tickets(10)

        # Revoke 20 tickets
        showing.revoke_tickets(20)

        # Revoking 20 seats should be rejected. Seats remaining should be 50 - 10 = 40
        self.assertEqual(showing.seats_remaining, 40)
