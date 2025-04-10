from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="app-main"),
    path("about/", views.about, name="app-about"),
    path("genres/", views.genres, name="app-genres"),
    path("genre/<int:genre_id>", views.genre_view, name="app-genre-view"),
    path("film/<int:film_id>", views.film_view, name="app-film-view"),
    path("director/<int:director_id>", views.director_view, name="app-director-view"),
]
