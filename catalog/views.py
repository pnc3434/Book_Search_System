# View-функции каталога книг.

from django.shortcuts import render

from books import find_book_by_id
from storage import load_books


def books(request):
    # Список книг — данные передаём в шаблон через контекст.
    books_list = load_books("data/books.json")
    context = {
        "books": books_list,
    }
    return render(request, "catalog/book_list.html", context)


def book_detail(request, book_id):
    # Карточка книги: находим объект и передаём в шаблон.
    books_list = load_books("data/books.json")
    book = find_book_by_id(books_list, book_id)
    context = {
        "book": book,
    }
    return render(
        request,
        "catalog/book_detail.html",
        context,
        status=404 if book is None else 200,
    )