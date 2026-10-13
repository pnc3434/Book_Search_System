# Корневая маршрутизация проекта bookreview.

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Админ-зона Django
    path("admin/", admin.site.urls),
    # Главная страница и корень "/"
    path("", include("homepage.urls")),
    # Префикс /books/ — всё, что внутри catalog.urls
    path("books/", include("catalog.urls")),
    # Префикс /reviews/ — всё, что внутри feedback.urls
    path("reviews/", include("feedback.urls")),
]

handler404 = "homepage.views.page_not_found"
