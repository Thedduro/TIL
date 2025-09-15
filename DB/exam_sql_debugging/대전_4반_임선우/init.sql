-- ===============================================================
-- 평가를 위한 DB 및 TABLE, DATA 생성 스크립트
-- ===============================================================

-- 1. DB 생성 및 선택
DROP DATABASE IF EXISTS ssafy_store_db;
CREATE DATABASE ssafy_store_db DEFAULT CHARACTER SET utf8mb4;
USE ssafy_store_db;

-- 2. Employees 테이블 생성 및 데이터 삽입
-- Employees: 직원 정보 테이블
--     employee_id: 직원 ID
--     name: 직원 이름
--     position: 직급
--     manager_id: 관리자 ID

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);

INSERT INTO Employees (employee_id, name, position, manager_id) VALUES
(1, '이영준', 'CEO', NULL),
(2, '박서진', '개발팀장', 1),
(3, '김민아', '디자인팀장', 1),
(4, '최수빈', '마케팅팀장', 1),
(5, '정다혜', '선임개발자', 2),
(6, '윤태영', '주임개발자', 2),
(7, '강지훈', '신입개발자', 2),
(8, '송예리', '선임디자이너', 3),
(9, '한유진', '주임디자이너', 3),
(10, '임도현', '마케터', 4),
(11, '서재현', '마케터', 4);

-- 3. Products 테이블 생성 및 데이터 삽입
-- Products: 상품 정보 테이블
--     product_id: 상품 ID
--     name: 상품 이름
--     category: 상품 카테고리
--     price: 상품 가격
--     stock: 재고 수량

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0
);

INSERT INTO Products (name, category, price, stock) VALUES
('기계식 키보드', '전자기기', 125000.00, 15),
('무선 마우스', '전자기기', 48000.00, 30),
('27인치 모니터', '전자기기', 350000.00, 10),
('USB-C 허브', '전자기기', 28000.00, 40),
('반팔 티셔츠', '의류', 29000.00, 50),
('후드 집업', '의류', 89000.00, 25),
('트레이닝 팬츠', '의류', 55000.00, 35),
('머그컵 세트', '생활용품', 18000.00, 80),
('에코백', '생활용품', 22000.00, 40),
('스마트폰 거치대', '생활용품', 13000.00, 60),
('고급 노트 세트', '문구류', 12000.00, 120),
('메탈 북엔드', '문구류', 19000.00, 70);

-- 4. Sales 테이블 생성 및 데이터 삽입
-- Sales: 판매 정보 테이블
--     sale_id: 판매 ID
--     employee_id: 직원 ID
--     product_id: 상품 ID
--     quantity: 판매 수량
--     sale_date: 판매 일자

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    product_id INT,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Sales (employee_id, product_id, quantity, sale_date) VALUES
(5, 1, 2, '2025-08-01'), (6, 2, 5, '2025-08-01'), (7, 11, 10, '2025-08-02'),
(8, 8, 20, '2025-08-03'), (5, 1, 3, '2025-08-04'), (6, 6, 2, '2025-08-05'),
(10, 9, 8, '2025-08-05'), (11, 5, 15, '2025-08-06'), (5, 7, 3, '2025-08-06'),
(7, 12, 12, '2025-08-07'), (8, 9, 5, '2025-08-07'), (10, 5, 20, '2025-08-08'),
(5, 2, 2, '2025-08-08'), (6, 3, 1, '2025-08-09'), (7, 4, 4, '2025-08-10'),
(8, 10, 10, '2025-08-11'), (11, 8, 15, '2025-08-12'), (5, 6, 3, '2025-08-13');

-- 스크립트 실행 완료 --