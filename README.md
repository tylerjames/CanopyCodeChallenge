# Canopy Growth Code Challenge

This code challenge involved creating an API for a movie theatre that could be used by admins to create viewing rooms, movies, and schedule showing; and by customers to purchase ticket to a listed showing.

## Current State

This was my first time really using Django, aside from a project in school around 12 years ago. I decided on using [Django REST Framework](https://www.django-rest-framework.org/) since it seemed to be quite popular and provided good support for creating REST APIs.

By reading documentation and following along with some tutorials I was able to create the models, views, serializers, and url patterns to create a basic API.

The exposed endpoints are these:

-   `/theatres`
    -   list all theatres (viewing rooms)
    -   add new theatres
-   `/movieListings/`
    -   view all movies playing across all theatres
-   `/theatres/<int:theatreId>/`
    -   view details for an individual theatre
-   `/theatres/<int:theatreId>/showings/`
    -   view all movies showing for a given theatre
-   `/theatres/<int:theatreId>/showings/<int:showingId>/`
    -   view details for a showing in a given theatre
-   `/theatres/<int:theatreId>/showings/<int:showingId>/tickets/`
    -   POST endpoint to purchase tickets

## Thoughts

Some things I would add or consider changing if I had more time:

-   I should be raising exceptions instead of returning error strings when appropriate
-   I need to add a `TheatreShowings` or `TheatreSchedule` class to make gather all the showings for a given theatre and to make sure that only one showing is scheduled per timeslot
-   I'd make things a bit more robust with some better input validation
-   I would consider using ViewSets instead of just Views since they seem to provide some benefits
-   I'd create an actual model for Ticket that had a unique ID and maybe some other details like `purchaseDate`
-   I'm not especially fond of the `/theatres/<int:theatreId>/showings/<int:showingId>/tickets/` endpoint for purchasing tickets. It would make more sense if there user accounts and it could list purchased tickets for the current user as well as allow them to purchase tickets. In such a case I wouldn't put the `tickets` route under the `theatres/showings` route.
-   The fact that it is so easy to add and run tests is really appealing. I've used frameworks before where it was a headache just to get started which made it more likely that tests would not be added

## Finally

It was interesting to explore Python and Django again. I'd forgotten how quirky Python is as a language – `if x is not None:` compared to `if (x != null)` for instance, or `snake_case` vs `camelCase`. I had an intersting time trying to map some Django concepts onto more familiar MVC patterns. It's odd that views/viewsets seem to function similar to controllers and that business logic is often put into serializers.

I'd like to explore testing a bit more as it's something that I don't have much experience with but I did not have much time to put into it.

**Thanks again for the opportunity!**
