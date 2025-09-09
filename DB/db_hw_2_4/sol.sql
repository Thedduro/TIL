UPDATE books 
SET price = 12.99
WHERE isbn = '9780743273565';

UPDATE books 
SET genre = 'Science Fiction'
WHERE isbn = '9780451524935';

UPDATE books 
SET publisher = "Charles Scribner's Sons"
WHERE isbn = '9780743273565';

SELECT * FROM books;