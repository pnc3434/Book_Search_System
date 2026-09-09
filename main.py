books = {
    "Война и мир": {
        "author": "Лев Толстой",
        "genre": "Роман",
        "rating": 4.5,
        "review_count": 2,
        "rating_sum": 9.0,
        "reviews": [
            {"user": "Анна", "text": "Гениально!", "rating": 5},
            {"user": "Иван", "text": "Слишком затянуто", "rating": 4}
        ]
    },
    "Преступление и наказание": {
        "author": "Фёдор Достоевский",
        "genre": "Роман",
        "rating": 4.8,
        "review_count": 1,
        "rating_sum": 4.8,
        "reviews": [
            {"user": "Мария", "text": "Потрясающая психология", "rating": 5}
        ]
    },
    "Мастер и Маргарита": {
        "author": "Михаил Булгаков",
        "genre": "Роман",
        "rating": 4.9,
        "review_count": 1,
        "rating_sum": 4.9,
        "reviews": [
            {"user": "Пётр", "text": "Любимая книга", "rating": 5}
        ]
    },
    "Собачье сердце": {
        "author": "Михаил Булгаков",
        "genre": "Повесть",
        "rating": 4.2,
        "review_count": 0,
        "rating_sum": 0.0,
        "reviews": []
    }
}

genres = {
    "Роман": ["Война и мир", "Преступление и наказание", "Мастер и Маргарита"],
    "Повесть": ["Собачье сердце"]
}

favorites = []   

def search_by_genre(genre):
    if genre in genres:
        return genres[genre]
    else:
        return []

def get_book_reviews(book_name):
    if book_name not in books:
        return "Книга не найдена"
    book = books[book_name]
    result = f"Книга: {book_name}\nАвтор: {book['author']}\nЖанр: {book['genre']}\nРейтинг: {book['rating']}\nВсего отзывов: {book['review_count']}\n"
    if book['review_count'] == 0:
        result += "Отзывов пока нет.\n"
    else:
        for i, review in enumerate(book['reviews'], 1):
            result += f"  {i}. {review['user']} – {review['rating']}: {review['text']}\n"
    return result

def add_to_favorites(book_name):
    if book_name not in books:
        return "Книга не найдена"
    if book_name in favorites:
        return f"Книга '{book_name}' уже в избранном"
    favorites.append(book_name)
    return f"Книга '{book_name}' добавлена в избранное"

if __name__ == "__main__":
    genre = "Роман"
    print(f"Книги в жанре '{genre}': {search_by_genre(genre)}")
    book = "Война и мир"
    print("\n" + get_book_reviews(book))
    print(add_to_favorites("Война и мир"))
    print(add_to_favorites("Война и мир"))
    print(f"Избранное: {favorites}")