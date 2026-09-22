from books import add_book
from favorites import add_to_favorites, remove_from_favorites


def make_book() -> tuple[list, int]:
    """Создать одну книгу и вернуть список и её id."""
    books: list = []
    book = add_book(books, "Мастер и Маргарита", "Булгаков", "Роман")
    return books, book.id


def test_add_to_favorites():
    books, book_id = make_book()
    favorites: list[int] = []
    assert add_to_favorites(books, favorites, book_id) == "Книга добавлена в избранное"
    assert book_id in favorites
    assert add_to_favorites(books, favorites, book_id) == "Книга уже в избранном"
    assert add_to_favorites(books, favorites, 999) == "Книга не найдена"


def test_remove_from_favorites():
    books, book_id = make_book()
    favorites = [book_id]
    assert remove_from_favorites(favorites, book_id) == "Книга удалена из избранного"
    assert remove_from_favorites(favorites, book_id) == "Книги нет в избранном"