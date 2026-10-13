# Маршруты отзывов.

from django.urls import path

from . import views

urlpatterns = [
    # /reviews/ — список отзывов
    path("", views.reviews, name="reviews"),
]
