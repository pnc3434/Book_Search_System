from books import find_book_by_id


def add_to_favorites(
    books: list[dict],
    favorites: list[int],
    book_id: int,
) -> str:
# Добавить книгу в избранное (по id)
    if find_book_by_id(books, book_id) is None:
        return "Книга не найдена"
    if book_id in favorites:
        return "Книга уже в избранном"
    favorites.append(book_id)
    return "Книга добавлена в избранное"

#   Удалить книгу из избранного
def remove_from_favorites(favorites: list[int], book_id: int) -> str:
    if book_id not in favorites:
        return "Книги нет в избранном"
    favorites.remove(book_id)
    return "Книга удалена из избранного"

# Вернуть текстовый список избранных книг
def show_favorites(books: list[dict], favorites: list[int]) -> str:
    if not favorites:
        return "Избранное пусто."
    lines = ["Избранные книги:"]
    for book_id in favorites:
        book = find_book_by_id(books, book_id)
        if book:
            lines.append(f"  [{book['id']}] {book['title']} — {book['author']}")
    return "\n".join(lines)