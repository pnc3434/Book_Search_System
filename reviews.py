from books import find_book_by_id

# Вернуть текстовое представление книги с отзывами
def get_book_reviews(books: list[dict], book_id: int) -> str:
    book = find_book_by_id(books, book_id)
    if book is None:
        return "Книга не найдена"

    result = (
        f"Книга: {book['title']}\n"
        f"Автор: {book['author']}\n"
        f"Жанр: {book['genre']}\n"
        f"Рейтинг: {book['rating']}\n"
        f"Всего отзывов: {len(book['reviews'])}\n"
    )
    if not book["reviews"]:
        result += "Отзывов пока нет.\n"
    else:
        for i, review in enumerate(book["reviews"], 1):
            result += (
                f"  {i}. {review['user']} – {review['rating']}★: "
                f"{review['text']}\n"
            )
    return result


def add_review(
    books: list[dict],
    book_id: int,
    user: str,
    text: str,
    rating: int,
) -> str:
# Добавить отзыв к книге и пересчитать средний рейтинг
    book = find_book_by_id(books, book_id)
    if book is None:
        return "Книга не найдена"
    if not 1 <= rating <= 5:
        return "Оценка должна быть от 1 до 5"

    book["reviews"].append({"user": user, "text": text, "rating": rating})
    ratings = [review["rating"] for review in book["reviews"]]
    book["rating"] = round(sum(ratings) / len(ratings), 2)
    return f"Отзыв от {user} добавлен к книге '{book['title']}'"

# Вернуть количество отзывов у книги
def get_review_count(books: list[dict], book_id: int) -> int:
    book = find_book_by_id(books, book_id)
    return len(book["reviews"]) if book else 0