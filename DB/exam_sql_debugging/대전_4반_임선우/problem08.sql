-- '의류' 또는 '문구류' 카테고리에 속하는 상품들의 판매 기록을 Sales 테이블에서 조회하려고 한다. 
-- 그러나 현재 쿼리는 오류가 발생한다.
-- 원인을 파악하고, 올바른 쿼리로 수정하시오.
-- 조회 할 컬럼명은 수정하지 않는다.

SELECT sale_id, product_id, quantity, sale_date
FROM Sales
WHERE product_id IN (
  SELECT product_id 
  FROM Products 
  WHERE category IN ('의류', '문구류')
  );
