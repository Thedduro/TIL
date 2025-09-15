-- Products 테이블에서 가격(price)이 가장 비싼 상품 3개의 이름과 가격을 조회하는 쿼리를 작성하시오.

SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 3;