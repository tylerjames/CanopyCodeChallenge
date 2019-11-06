from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movietheatre.boxoffice.models import *
from movietheatre.boxoffice.serializers import *


# Create your views here.
class MovieList(APIView):
    """
    List  all movie titles
    """

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieView(APIView):
    """
    View for a single movie
    """

    def getMovie(self, movieId):
        try:
            return Movie.objects.get(pk=movieId)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, movieId):
        movie = self.getMovie(movieId)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TheatreListView(APIView):
    """
    Lists all theatres
    """

    def get(self, request):
        theatres = Theatre.objects.all()
        serializer = TheatreSerializer(theatres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TheatreSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TheatreView(APIView):
    """
    View for a single theatre
    """

    def get_theatre(self, theatre_id):
        try:
            return Theatre.objects.get(pk=theatre_id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, theatreId):
        theatre = self.get_theatre(theatreId)
        serializer = TheatreSerializer(theatre)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowingListView(APIView):
    """
    Displays all showings
    """

    def get(self, request, theatreId=None):
        print(f"Got request with theatre ID: {theatreId}")
        showings = Showing.objects.all()
        if theatreId is not None:
            showings = showings.filter(theatre__id=theatreId)

        serializer = ShowingOutputSerializer(showings, many=True)
        return Response(serializer.data)

    def post(self, request, theatreId):
        serializer = ShowingInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShowingView(APIView):
    """
    View for a single showing
    """

    def get(self, request, theatreId, showingId):
        if theatreId is None:
            return Response("Missing theatreId", status=status.HTTP_400_BAD_REQUEST)
        if showingId is None:
            return Response("Missing showingId", status=status.HTTP_400_BAD_REQUEST)

        showing = Showing.objects.get(pk=showingId, theatre__id=theatreId)
        print(f"Got showing: {showing}")

        serializer = ShowingOutputSerializer(showing)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TicketsView(APIView):
    """
    View for booking tickets to a movie showing
    """

    def get(self, request, theatreId, showingId):
        if showingId is None:
            return Response("Must specify a showing", status=status.HTTP_400_BAD_REQUEST)

        showing = Showing.objects.get(pk=showingId)
        if showing is None:
            return Response("No showing matched id", status=status.HTTP_400_BAD_REQUEST)

        return Response(f"There are {showing.seats_remaining} for the movie")

    def post(self, request, theatreId, showingId):
        if showingId is None:
            return Response("Must specify a showing", status=status.HTTP_400_BAD_REQUEST)

        ticket_count = request.data["count"]
        print(f"Got ticket count: {ticket_count}")
        if ticket_count <= 0:
            return Response("Number of tickets requested must be greater than zero", status=status.HTTP_400_BAD_REQUEST)

        showing = Showing.objects.get(pk=showingId)
        if showing is None:
            return Response("No showing matched id", status=status.HTTP_400_BAD_REQUEST)

        if ticket_count > showing.seats_remaining:
            return Response(f"Error: Not enough seats available to issue {ticket_count} tickets. There are {showing.seats_remaining} seats left", status=status.HTTP_400_BAD_REQUEST)

        showing.issue_tickets(ticket_count)
        showing.save()
        return Response(f"{ticket_count} tickets issued", status=status.HTTP_400_BAD_REQUEST)
