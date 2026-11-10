-- 1. Список всех книг (SELECT)
SELECT id, title, author, genre FROM books ORDER BY title;

-- 2. Список книг с жанром "Роман" (WHERE)
SELECT title, author FROM books WHERE genre = 'Роман' ORDER BY title;

-- 3. Поиск книг с рейтингом выше заданного (WHERE + подзапрос)
SELECT title FROM books 
WHERE id IN (
    SELECT book_id FROM reviews GROUP BY book_id HAVING AVG(rating) > 4
);

-- 4. Полная информация об отзывах с названием книги (JOIN)
SELECT r.id, r.user_name, r.rating, r.text, b.title AS book_title
FROM reviews r
JOIN books b ON r.book_id = b.id
ORDER BY r.id;

-- 5. Книги, у которых есть отзывы (JOIN)
SELECT DISTINCT b.title 
FROM books b
JOIN reviews r ON b.id = r.book_id;

-- 6. Общее количество отзывов в базе (COUNT)
SELECT COUNT(*) AS total_reviews FROM reviews;

-- 7. Количество книг каждого жанра (GROUP BY)
SELECT genre, COUNT(*) AS books_count 
FROM books 
GROUP BY genre 
ORDER BY books_count DESC;

-- 8. Средний рейтинг каждой книги (GROUP BY, AVG)
SELECT b.title, ROUND(AVG(r.rating), 2) AS avg_rating
FROM books b
LEFT JOIN reviews r ON b.id = r.book_id
GROUP BY b.id, b.title
ORDER BY avg_rating DESC;

-- 9. Книги, у которых 2 и более отзывов (HAVING)
SELECT b.title, COUNT(r.id) AS review_count
FROM books b
JOIN reviews r ON b.id = r.book_id
GROUP BY b.id, b.title
HAVING COUNT(r.id) >= 2;

-- 10. Топ-3 книги по количеству отзывов (LIMIT)
SELECT b.title, COUNT(r.id) AS review_count
FROM books b
LEFT JOIN reviews r ON b.id = r.book_id
GROUP BY b.id, b.title
ORDER BY review_count DESC
LIMIT 3;