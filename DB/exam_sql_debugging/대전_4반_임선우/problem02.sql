-- '전자기기' 카테고리 상품 중, 가격이 10만원 이상이거나 재고가 20개 미만인 상품을 조회하려 한다. 
-- 그러나 아래 쿼리는 의도와 다른 결과를 반환하고 있다.
-- 원인을 파악하고, 올바른 쿼리로 수정하시오.
-- 조회 할 컬럼명은 수정하지 않는다.

SELECT name, category, price, stock
FROM Products
WHERE (category = '전자기기' AND price >= 100000) OR (category = '전자기기' AND stock < 20);
