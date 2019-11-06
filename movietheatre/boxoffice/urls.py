from django.urls import path

from movietheatre.boxoffice import views

urlpatterns = [
    path('theatres/', views.TheatreListView.as_view()),
    path('theatres/<int:theatreId>/', views.TheatreView.as_view()),
    path('theatres/<int:theatreId>/showings/', views.ShowingListView.as_view()),
    path('theatres/<int:theatreId>/showings/<int:showingId>/',
         views.ShowingView.as_view()),
    path('theatres/<int:theatreId>/showings/<int:showingId>/tickets/',
         views.TicketsView.as_view()),
    path('movieListings/', views.ShowingListView.as_view()),
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:movieId>/', views.MovieView.as_view())
]
