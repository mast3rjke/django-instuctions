from django.shortcuts import render
from random import randint


# Create your views here.
def main(request):
    return render(
        request, "app_1/main.html", {"title": "Главная"}
    )


def about(request):
    return render(
        request, "app_1/about.html", {"title": "О Нас"}
    )
