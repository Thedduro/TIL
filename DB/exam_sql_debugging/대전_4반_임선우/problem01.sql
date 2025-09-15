-- '의류' 카테고리에 속하는 모든 상품의 가격을 5% 인상하는 UPDATE 쿼리를 작성하시오.
UPDATE products
SET price = price*1.05
WHERE category = '의류';