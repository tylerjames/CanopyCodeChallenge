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
