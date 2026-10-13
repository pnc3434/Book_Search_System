# View-функции отзывов.

from django.http import HttpResponse

from homepage.views import page   # общий каркас страницы
from storage import load_books    # загрузка книг из JSON


def reviews(request):
    # Список всех отзывов по всем книгам.
    books_list = load_books("data/books.json")

    items = ""
    count = 0
    for book in books_list:
        for review in book.reviews:
            count += 1
            items += (
                f'<li class="list-group-item">'
                f"<strong>{book.title}</strong>: "
                f"{review.user} — {review.rating}★ "
                f"«{review.text}» "
                f'<a href="/books/{book.id}/" '
                f'class="btn btn-sm btn-outline-primary">'
                f"к книге</a>"
                f"</li>"
            )

    if count == 0:
        items = (
            '<li class="list-group-item">'
            "Отзывов пока нет."
            "</li>"
        )

    content = f"""
    <h1>Отзывы</h1>
    <p>Всего отзывов: {count}</p>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Отзывы — Система книжных отзывов", content))
