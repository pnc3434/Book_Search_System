# View-функции каталога книг, работающие с SQLite.

from django.shortcuts import render
from db.database import get_connection


def books(request):
    # Список всех книг с их рейтингом.
    conn = get_connection()
    # Используем запрос с LEFT JOIN и GROUP BY
    books_list = conn.execute("""
        SELECT b.id, b.title, b.author, b.genre, 
               ROUND(AVG(r.rating), 2) AS rating
        FROM books b
        LEFT JOIN reviews r ON b.id = r.book_id
        GROUP BY b.id, b.title
        ORDER BY b.title;
    """).fetchall()
    conn.close()

    context = {"books": books_list}
    return render(request, "catalog/book_list.html", context)


def book_detail(request, book_id):
    # Карточка книги с отзывами.
    conn = get_connection()
    
    # Ищем саму книгу
    book = conn.execute(
        "SELECT * FROM books WHERE id = ?", [book_id]
    ).fetchone()
    
    # Ищем её отзывы
    reviews = []
    if book:
        reviews = conn.execute(
            "SELECT * FROM reviews WHERE book_id = ? ORDER BY id", 
            [book_id]
        ).fetchall()
    
    conn.close()

    context = {"book": book, "reviews": reviews}
    return render(
        request,
        "catalog/book_detail.html",
        context,
        status=404 if book is None else 200,
    )


def book_search(request):
    # Поиск книг по минимальному рейтингу.
    min_rating = request.GET.get("rating")
    books_list = []
    
    if min_rating:
        try:
            # Преобразуем строку из формы в число (float)
            rating_value = float(min_rating)
            
            conn = get_connection()
            # Используем CAST для надежного сравнения чисел в SQLite
            books_list = conn.execute("""
                SELECT title, author FROM books 
                WHERE id IN (
                    SELECT book_id FROM reviews 
                    GROUP BY book_id 
                    HAVING CAST(AVG(rating) AS REAL) >= ?
                )
            """, [rating_value]).fetchall()
            conn.close()
        except ValueError:
            # Если ввели не число — просто игнорируем
            pass
        
    context = {
        "books": books_list,
        "min_rating": min_rating,
    }
    return render(request, "catalog/book_search.html", context)