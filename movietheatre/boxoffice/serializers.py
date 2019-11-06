from rest_framework import serializers

from movietheatre.boxoffice.models import Movie, Showing, Theatre


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ['id', 'seats']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']


class ShowingInputSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    theatre = serializers.PrimaryKeyRelatedField(
        queryset=Theatre.objects.all())

    class Meta:
        model = Showing
        fields = ['id', 'movie', 'theatre', 'timeslot']


class ShowingOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showing
        fields = ['id', 'movie', 'theatre', 'show_time', 'seats_remaining']
        depth = 1
