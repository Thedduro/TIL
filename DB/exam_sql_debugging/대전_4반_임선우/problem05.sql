-- 각 판매 담당자(employee_id)별로 총 판매 수량(quantity)의 합을 구하고, 그 합이 10개를 초과하는 담당자만 조회하려 한다. 
-- 그러나 현재 쿼리는 오류가 발생한다.
-- 원인을 파악하고, 올바른 쿼리로 수정하시오.
-- 조회 할 컬럼명은 수정하지 않는다.

SELECT employee_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY employee_id
HAVING total_quantity > 10;
