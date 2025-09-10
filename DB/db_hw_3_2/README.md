### 학습 주제
- 데이터베이스 인덱스 및 JOIN 연산자 활용

---

### 학습 목표
- 인덱스의 개념과 종류를 이해하고, 데이터베이스에서 인덱스를 생성하고 사용하는 방법을 익힌다.  
- 여러 테이블을 조인하여 데이터를 검색하는 방법을 이해하고, INNER JOIN의 사용법을 익힌다.  

---

### 학습 개념
- **인덱스(Index)**  
  - 데이터베이스 테이블에서 검색 속도를 향상시키기 위해 사용하는 데이터 구조.  
  - 특정 열에 대해 생성되며, 해당 열의 값을 기반으로 데이터의 위치를 빠르게 찾을 수 있도록 한다.  
  - 일반적으로 **B-트리 형태**로 구현된다.  

- **클러스터드 인덱스(Clustered Index)**  
  - 테이블의 데이터가 인덱스에 의해 물리적으로 정렬되는 인덱스.  
  - 하나의 테이블에는 하나의 클러스터드 인덱스만 생성할 수 있다.  
  - 주로 **기본 키**에 대해 생성된다.  

- **비클러스터드 인덱스(Non-Clustered Index)**  
  - 테이블의 데이터가 인덱스에 의해 물리적으로 정렬되지 않는 인덱스.  
  - 하나의 테이블에는 여러 개의 비클러스터드 인덱스를 생성할 수 있다.  
  - **자주 검색되는 열**에 대해 생성된다.  

- **JOIN 연산자**  
  - 두 개 이상의 테이블을 결합하여 데이터를 검색하는 데 사용된다.  
  - 여러 종류가 있으며, 가장 일반적인 것은 **INNER JOIN**이다.  

- **INNER JOIN**  
  - 두 테이블 간의 공통된 열을 기준으로 일치하는 행만 반환한다.  
  - 두 테이블 모두에서 일치하는 데이터가 있을 때만 결과를 반환한다.  

---

### 학습 방향
- 인덱스의 개념과 종류를 이해하고, 인덱스를 생성하고 사용하는 방법을 학습한다.  
- 인덱스를 사용하여 데이터베이스의 검색 성능을 향상시키는 방법을 익힌다.  
- 여러 테이블을 조인하여 데이터를 검색하는 방법을 학습한다.  
- 다양한 인덱스 생성 및 사용 예제를 통해 쿼리 작성 능력을 향상시키고, 이를 실제 프로젝트에 적용할 수 있도록 한다.  

---

### 문제 의도
- 학생들이 데이터베이스 인덱스의 개념과 사용법을 이해하고, 실제로 인덱스를 생성하고 사용하는 방법을 익히도록 하기 위함이다.  

---

### 사전 지식
- 기본적인 SQL 문법  
- 데이터베이스 테이블 생성 및 데이터 삽입  
- `SELECT` 문을 사용한 데이터 검색  
- 인덱스의 기본 개념  

---

### 문제 핵심
- 인덱스를 생성하고 사용하는 방법을 이해하는 것  
- 인덱스를 사용하여 데이터베이스의 검색 성능을 최적화하는 방법을 실습하는 것  
- 인덱스를 활용하여 특정 조건을 만족하는 데이터를 검색하는 방법을 익히는 것  

---

### 문제
- 도서 정보를 저장할 수 있는 DB를 구축한다.  
- 보유한 데이터는 책, 작가, 장르 데이터이다.  
- 각각의 데이터를 **정규화 양식**에 맞춰 삽입할 수 있도록 적절한 테이블을 구성하고, 데이터를 삽입한다.  

---

### 요구사항
- `library_db`를 생성하고 활용한다.  
- `books`, `authors`, `genres` 테이블을 생성한다.  

**authors 테이블**
- 저자 정보를 저장한다.  
- 컬럼  
  - `id` (정수형, 자동 증가, 기본 키)  
  - `name` (문자열형, 최대 100자)  
- 삽입 데이터  
  - J.K. Rowling  
  - George R.R. Martin  
  - J.R.R. Tolkien  
  - Isaac Asimov  
  - Agatha Christie  

**genres 테이블**
- 장르 정보를 저장한다.  
- 컬럼  
  - `id` (정수형, 자동 증가, 기본 키)  
  - `genre_name` (문자열형, 최대 100자)  
- 삽입 데이터  
  - Fantasy  
  - Science Fiction  
  - Mystery  
  - Thriller  

**books 테이블**
- 책 정보를 저장한다.  
- 컬럼  
  - `id` (정수형, 자동 증가, 기본 키)  
  - `title` (문자열형, 최대 100자)  
  - `author_id` (정수형, authors 테이블의 id와 외래 키 관계)  
  - `genre_id` (정수형, genres 테이블의 id와 외래 키 관계)  
- 삽입 데이터  
  - ('Harry Potter and the Philosopher''s Stone', J.K. Rowling의 id, Fantasy의 id)  
  - ('Harry Potter and the Chamber of Secrets', J.K. Rowling의 id, Fantasy의 id)  
  - ('A Game of Thrones', George R.R. Martin의 id, Fantasy의 id)  
  - ('A Clash of Kings', George R.R. Martin의 id, Fantasy의 id)  
  - ('The Hobbit', J.R.R. Tolkien의 id, Fantasy의 id)  
  - ('The Lord of the Rings', J.R.R. Tolkien의 id, Fantasy의 id)  
  - ('Foundation', Isaac Asimov의 id, Science Fiction의 id)  
  - ('I, Robot', Isaac Asimov의 id, Science Fiction의 id)  
  - ('Murder on the Orient Express', Agatha Christie의 id, Mystery의 id)  
  - ('The Mysterious Affair at Styles', Agatha Christie의 id, Mystery의 id)  
  - ('The Girl with the Dragon Tattoo', Agatha Christie의 id, Thriller의 id)  
