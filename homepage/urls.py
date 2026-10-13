# Маршруты главной страницы.

from django.urls import path

from . import views

app_name = "homepage"  # пространство имён приложения

urlpatterns = [
    path("", views.index, name="index"),
]