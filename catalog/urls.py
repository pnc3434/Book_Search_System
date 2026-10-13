# Маршруты каталога книг.

from django.urls import path

from . import views

app_name = "catalog"  # пространство имён приложения

urlpatterns = [
    path("", views.books, name="books"),
    path("<int:book_id>/", views.book_detail, name="book_detail"),
]