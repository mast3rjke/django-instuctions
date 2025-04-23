from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . import models


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = "__all__"
        labels = {
            "name": "Название жанра"
        }


class DirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = "__all__"
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "second_name": "Отчество"
        }


class FilmForm(forms.ModelForm):
    poster_url = forms.CharField()

    class Meta:
        model = models.Film
        fields = "__all__"
        labels = {
            "name": "Название",
            "descriptions": "Описание",
            "poster_url": "Ссылка на постер",
            "genre": "Жанр",
            "director": "Режиссер"
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=50,
        help_text="Адрес электронной почты пользователя"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
