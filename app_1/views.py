from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app_1.models import Genre


# Create your views here.
def main(request):
    return render(
        request, "app_1/main.html", {"title": "Главная"}
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
