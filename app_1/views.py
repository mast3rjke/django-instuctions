from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from app_1 import forms, views_helpers, models


# Create your views here.
def main(request):
    return render(
        request, "app_1/main.html", {
            "title": "Главная",
            "films": models.Film.objects.all(),
            "directors": models.Director.objects.all(),
            "genres": models.Genre.objects.all(),
        }
    )


def view_genre(request, genre_id: int):
    return views_helpers.base_view(
        request, models.Genre, genre_id, "genre",
        {
            "header_creator": lambda entity: f"Жанр {entity.name}" if entity else "Нет такого жанра",
            "additional_data": ["films", "directors"]
        }
    )


def view_film(request, film_id: int):
    return views_helpers.base_view(
        request, models.Film, film_id, "film",
        {
            "header_creator": lambda entity: f"Фильм \"{entity.name}\"" if entity else "Нет такого фильма"
        }
    )


def view_director(request, director_id: int):
    return views_helpers.base_view(
        request, models.Director, director_id, "director", {
            "header_creator": lambda entity: f"Режиссер \"{entity.render_name}\"" if entity else "Нет такого режиссера",
            "additional_data": ["films", "genres"]
        }
    )


def create_genre(request):
    return views_helpers.base_create_page(request, forms.GenreForm)


def create_film(request):
    return views_helpers.base_create_page(request, forms.FilmForm)


def create_director(request):
    return views_helpers.base_create_page(request, forms.DirectorForm)


def delete_genre(_, genre_id):
    return views_helpers.base_delete_entity(models.Genre, genre_id)


def delete_film(_, film_id):
    return views_helpers.base_delete_entity(models.Film, film_id)


def delete_director(_, director_id):
    return views_helpers.base_delete_entity(models.Director, director_id)


def edit_genre(request, genre_id):
    return views_helpers.base_edit_page(request, forms.GenreForm, models.Genre, genre_id)


def edit_film(request, film_id):
    return views_helpers.base_edit_page(request, forms.FilmForm, models.Film, film_id)


def edit_director(request, director_id):
    return views_helpers.base_edit_page(request, forms.DirectorForm, models.Director, director_id)


def register_view(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("app-main")
    else:
        form = forms.RegistrationForm()

    return render(
        request,
        "app_1/entity_form_page.html",
        {"form": form}
    )


def login_view(request):
    form = forms.LoginForm(data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("app-main")

    return render(
        request,
        "app_1/entity_form_page.html",
        {"form": form}
    )


def logout_view(request):
    logout(request)

    return redirect("app-main")


