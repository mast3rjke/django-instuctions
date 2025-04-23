from django.urls import path
from . import views


def _add_path(entity_name: str, operation_prefix: str):
    url: str = f"{entity_name}/{operation_prefix}"

    if operation_prefix != "create":
        url += f"/<int:{entity_name}_id>"

    return path(
        url,
        getattr(views, f"{operation_prefix}_{entity}"),
        name=f"app-{entity}-{operation_prefix}"
    )


urlpatterns = [
    path("", views.main, name="app-main"),
    path("register/", views.register_view, name="app-register"),
    path("login/", views.login_view, name="app-login"),
    path("logout/", views.logout_view, name="app-logout"),
]

entities: list[str] = ["genre", "film", "director"]
operations: list[str] = ["view", "create", "edit", "delete"]

for entity in entities:
    for operation in operations:
        urlpatterns.append(
            _add_path(entity, operation)
        )
