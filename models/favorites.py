from typing import List

from models.book import Book
from books import find_book_by_id


def add_to_favorites(
    books: List[Book],
    favorites: List[int],
    book_id: int,
) -> str:
    # Добавить книгу в избранное
    if find_book_by_id(books, book_id) is None:
        return "Книга не найдена"
    if book_id in favorites:
        return "Книга уже в избранном"
    favorites.append(book_id)
    return "Книга добавлена в избранное"


def remove_from_favorites(favorites: List[int], book_id: int) -> str:
    # Удалить книгу из избранного
    if book_id not in favorites:
        return "Книги нет в избранном"
    favorites.remove(book_id)
    return "Книга удалена из избранного"


def show_favorites(books: List[Book], favorites: List[int]) -> str:
    # Показать список избранных книг
    if not favorites:
        return "Избранное пусто."
    lines = ["Избранные книги:"]
    for book_id in favorites:
        book = find_book_by_id(books, book_id)
        if book:
            lines.append(f"  {book}")
    return "\n".join(lines)