-- 데이터베이스 생성
CREATE DATABASE libraries;

-- 데이터베이스 사용
USE libraries;

-- books 테이블 생성
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publisher VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    published_date DATE NOT NULL,
    isbn VARCHAR(13) NOT NULL UNIQUE,
    price DECIMAL(5,2) NOT NULL,
    genre VARCHAR(50) NOT NULL
);
