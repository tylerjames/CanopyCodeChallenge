from django.contrib import admin

from .models import Movie, Showing, Theatre

# Register your models here.
admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Showing)
