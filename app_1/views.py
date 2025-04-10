from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app_1.models import Genre, Film, Director


# Create your views here.
def main(request):
    return render(
        request, "app_1/main.html", {
            "title": "Главная",
            "films": Film.objects.all(),
            "directors": Director.objects.all(),
            "genres": Genre.objects.all(),
        }
    )


def about(request):
    return render(
        request, "app_1/about.html", {"title": "О Нас"}
    )


@login_required
def genres(request):
    all_genres = Genre.objects.all()
    return render(
        request, "app_1/genres.html", {
            "title": "Жанры",
            "genres": all_genres
        }
    )


def genre_view(request, genre_id: int):
    try:
        genre = Genre.objects.get(pk=genre_id)
    except Genre.DoesNotExist:
        genre = None

    return render(
        request, "app_1/genre_view.html", {
            "title": f"Жанр {genre.name}" if genre else "Нет такого жанра",
            "genre": genre,
            "films": genre.films if genre else None,
            "directors": genre.directors if genre else None
        }
    )


def film_view(request, film_id: int):
    try:
        film = Film.objects.get(pk=film_id)
    except Film.DoesNotExist:
        film = None

    return render(
        request, "app_1/film_view.html", {
            "title": f"Фильм \"{film.name}\"" if film else "Нет такого фильма",
            "film": film
        }
    )


def director_view(request, director_id: int):
    try:
        director = Director.objects.get(pk=director_id)
    except Director.DoesNotExist:
        director = None

    return render(
        request, "app_1/director_view.html", {
            "title": f"Режиссер \"{director.render_name}\"" if director else "Нет такого режиссера",
            "director": director,
            "films": director.films,
            "genres": director.genres
        }
    )