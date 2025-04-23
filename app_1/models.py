from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)

    @property
    def directors(self) -> list:
        added_directors: list[str] = []
        directors: list = []

        for film in self.films:
            if film.director.render_name not in added_directors:
                directors.append(film.director)
                added_directors.append(film.director.render_name)

        return directors

    @property
    def films(self):
        return Film.objects.filter(genre=self)

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)

    @property
    def render_name(self) -> str:
        director_item_name: str = f"{self.last_name} {self.first_name}"

        if self.second_name:
            director_item_name += f" {self.second_name}"

        return director_item_name

    @property
    def genres(self) -> list:
        added_genres: list[str] = []
        genres: list = []

        for film in self.films:
            if film.genre.name not in added_genres:
                genres.append(film.genre)
                added_genres.append(film.genre.name)

        return genres

    @property
    def films(self):
        return Film.objects.filter(director=self)

    def __str__(self) -> str:
        return self.render_name


class Film(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField(null=True)
    poster_url = models.TextField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.name

