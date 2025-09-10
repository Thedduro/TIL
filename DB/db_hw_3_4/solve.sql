-- 1. 인덱스 생성
CREATE INDEX idx_authors_name ON authors(name);
CREATE INDEX idx_genres_name ON genres(genre_name);

-- 2. INNER JOIN을 활용한 조회문
SELECT 
    b.title AS book_title,
    a.name AS author_name,
    g.genre_name AS genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id
WHERE a.name = 'J.K. Rowling'
  AND g.genre_name = 'Fantasy';