from typing import List, Optional

from models.review import Review


class Book:
    # Книга с отзывами и средним рейтингом

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        genre: str,
        reviews: Optional[List[Review]] = None,
    ) -> None:
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.reviews: List[Review] = reviews or []
        self.rating: float = self._calculate_rating()

    def _calculate_rating(self) -> float:
        # Пересчитать средний рейтинг по отзывам
        if not self.reviews:
            return 0.0
        total = sum(review.rating for review in self.reviews)
        return round(total / len(self.reviews), 2)

    def add_review(self, review: Review) -> None:
        # Добавить отзыв и пересчитать рейтинг
        self.reviews.append(review)
        self.rating = self._calculate_rating()

    def is_suitable_genre(self, genre: str) -> bool:
        return self.genre.lower() == genre.lower()

    def __str__(self) -> str:

        return (
            f"[{self.id}] {self.title} — {self.author} "
            f"({self.genre}), рейтинг: {self.rating}"
        )

    @classmethod
    def from_data(cls, data: dict) -> "Book":
        # Создать книгу из словаря (с отзывами)
        reviews = [Review.from_data(r) for r in data.get("reviews", [])]
        return cls(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            reviews=reviews,
        )

    def to_data(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "rating": self.rating,
            "reviews": [r.to_data() for r in self.reviews],
        }