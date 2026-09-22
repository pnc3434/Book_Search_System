from typing import List

from models.review import Review


def get_review_count(reviews: List[Review]) -> int:
    # Вернуть количество отзывов
    return len(reviews)