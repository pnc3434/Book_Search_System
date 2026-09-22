import pytest

from models.review import Review


def test_review_creation():
    review = Review("Анна", "Отлично!", 5)
    assert review.user == "Анна"
    assert review.rating == 5
    assert "Анна" in str(review)


def test_review_invalid_rating():
    with pytest.raises(ValueError):
        Review("Анна", "Плохо", 10)


def test_review_from_data():
    data = {"user": "Иван", "text": "Хорошо", "rating": 4}
    review = Review.from_data(data)
    assert review.user == "Иван"
    assert review.rating == 4