from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)

    @property
    def format_name(self) -> str:
        return f'12{self.name}12'

    def __str__(self) -> str:
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        director_item_name: str = f"{self.last_name} {self.first_name}"

        if self.second_name:
            director_item_name += f" {self.second_name}"

        return director_item_name


class Film(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.name
