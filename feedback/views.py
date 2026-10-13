# View-функции отзывов.

from django.shortcuts import render

from storage import load_books


def reviews(request):
    # Собираем все отзывы по всем книгам в плоский список.
    books_list = load_books("data/books.json")

    reviews_list = []
    for book in books_list:
        for review in book.reviews:
            reviews_list.append({
                "book_id": book.id,
                "book_title": book.title,
                "user": review.user,
                "text": review.text,
                "rating": review.rating,
            })

    context = {
        "reviews": reviews_list,
    }
    return render(request, "feedback/review_list.html", context)