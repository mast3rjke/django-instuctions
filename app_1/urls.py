from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="app-main"),
    path("about/", views.about, name="app-about")
]
