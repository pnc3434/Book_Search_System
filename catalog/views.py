# View-функции каталога книг.

from django.http import HttpResponse

from books import find_book_by_id  # функция поиска из ПР3
from homepage.views import page     # общий каркас страницы
from storage import load_books      # загрузка книг из JSON


def books(request):
    # Список всех книг из data/books.json
    books_list = load_books("data/books.json")

    # Формируем HTML-элементы списка
    items = ""
    for book in books_list:
        text = (
            f"{book.title} — {book.author} "
            f"({book.genre}), рейтинг: {book.rating}"
        )
        items += (
            f'<li class="list-group-item">'
            f'<a href="/books/{book.id}/">{text}</a>'
            f"</li>"
        )

    content = f"""
    <h1>Книги</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Книги — Система книжных отзывов", content))


def book_detail(request, book_id):
    # Карточка книги с отзывами.
    books_list = load_books("data/books.json")
    book = find_book_by_id(books_list, book_id)

    # Если книги с таким id нет — отдаём 404
    if book is None:
        content = """
        <h1 class="text-danger">Книга не найдена</h1>
        <a href="/books/" class="btn btn-outline-secondary">
            ← к списку книг
        </a>
        """
        return HttpResponse(
            page("Книга не найдена", content),
            status=404,
        )

    # Формируем блок отзывов
    reviews_html = ""
    if book.reviews:
        for review in book.reviews:
            reviews_html += (
                f'<li class="list-group-item">'
                f"<strong>{review.user}</strong> — "
                f"{review.rating}★: {review.text}"
                f"</li>"
            )
    else:
        reviews_html = (
            '<li class="list-group-item">'
            "Отзывов пока нет."
            "</li>"
        )

    content = f"""
    <div class="card mb-3">
        <div class="card-body">
            <h5 class="card-title">{book.title}</h5>
            <p class="card-text">
                <strong>Автор:</strong> {book.author}<br>
                <strong>Жанр:</strong> {book.genre}<br>
                <strong>Рейтинг:</strong> {book.rating}<br>
                <strong>Всего отзывов:</strong>
                {len(book.reviews)}
            </p>
            <a href="/books/" class="btn btn-outline-secondary">
                ← к списку книг
            </a>
        </div>
    </div>
    <h4>Отзывы</h4>
    <ul class="list-group">{reviews_html}</ul>
    """
    return HttpResponse(page(book.title, content))
