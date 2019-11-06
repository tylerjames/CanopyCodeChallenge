# Movie Theatre Implementation

## Assumptions

Given that this is an exercise and not a real-world system I'm going to make some assumptions based on the stated requirements.

> Movies that are playing at a set time every day

From this I will make a few assumptions:

1. There are fixed timeslots when movies are shown
2. A movie fits into a timeslot nicely – there are no movies that require 1.5 timeslots, for instance
3. The theatre is open from 8:00am - 12:00am (16 hrs) and that each timeslot 2 hours long and thus there are **8 timeslots** for showings (let's say each movie is 90 mins which leaves time for audience changeover, cleanup, preparation for next showing)

> Tickets that are sold to customers

1. There are no assigned seats. If a customer wants 2 tickets the system will not figure out if there are 2 adjacent seats available. Selling a ticket will simply decrement the number of available seats.

## Constraints

1. Two `Movies` cannot be scheduled in the same timeslot in the same `Theatre`
2. You cannot issue more tickets than there are seats in a `Theatre`
3. You cannot revoke more tickets than have actually been sold.
4. You should not be able to reduce the number of seats in a Theatre after tickets have been sold.

## Notes

-   need a TheatreSchedule that connects Theatres to showings
-   booking needs to be based on availability

## Making a booking

-   request a ticket based on theatre, movie, and timeslot
-   Causes for failure: - timeslot, movie, or theatre don't exist - theatre is full - movie is not showing a specified timeslot and theatre
