# Маршруты каталога книг.

from django.urls import path

from . import views

urlpatterns = [
    # /books/ — список книг
    path("", views.books, name="books"),
    # /books/<id>/ — карточка книги; id передаётся во view
    path("<int:book_id>/", views.book_detail, name="book_detail"),
]
