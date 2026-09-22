from typing import List


class Review:

    def __init__(self, user: str, text: str, rating: int) -> None:
    #  Создать объект отзыва.
        if not 1 <= rating <= 5:
            raise ValueError("Оценка должна быть от 1 до 5")
        self.user = user
        self.text = text
        self.rating = rating

    def __str__(self) -> str:
        # Строковое представление отзыва.
        return f"{self.user} – {self.rating}★: {self.text}"

    @classmethod
    def from_data(cls, data: dict) -> "Review":
        # Создать отзыв из словаря (для загрузки из JSON)
        return cls(
            user=data["user"],
            text=data["text"],
            rating=data["rating"],
        )

    def to_data(self) -> dict:
    # Преобразовать объект в словарь (для сохранения в JSON)
        return {
            "user": self.user,
            "text": self.text,
            "rating": self.rating,
        }


def get_review_count(reviews: List[Review]) -> int:
    return len(reviews)