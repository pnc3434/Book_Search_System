# Маршруты отзывов.

from django.urls import path

from . import views

app_name = "feedback"  # пространство имён приложения

urlpatterns = [
    path("", views.reviews, name="reviews"),
]