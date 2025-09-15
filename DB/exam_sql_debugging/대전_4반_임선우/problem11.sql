-- Products 테이블의 각 상품에 대해, 해당 상품의 카테고리 내에서 가장 비싼 제품인지 여부를 확인하는 쿼리를 작성하시오.
-- 조회 컬럼: product_id, name, category, price
-- 조건: 해당 상품의 가격이 같은 카테고리에 속한 모든 상품의 최대 가격과 일치해야 한다.

SELECT  product_id, name, category, price
FROM products
WHERE products.price IN (SELECT max(price)
FROM products
GROUP BY category);
