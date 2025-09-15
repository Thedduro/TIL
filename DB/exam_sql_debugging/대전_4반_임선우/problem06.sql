-- 모든 직원의 이름과 해당 직원이 올린 판매 건수(sale_id의 개수)를 조회하려고 한다. 
-- 단, 아직 판매 실적이 없는 직원도 목록에 포함되어야 한다. 
-- 아래 쿼리는 판매 실적이 있는 직원만 조회하고 있다.
-- 판매 실적이 없는 직원도 결과에 포함되도록(판매 건수는 0으로 표시) 쿼리를 수정하시오.
-- 조회 할 컬럼명은 수정하지 않는다.

SELECT e.name, COUNT(s.sale_id) AS sales_count
FROM Employees e
LEFT JOIN Sales s 
ON e.employee_id = s.employee_id
GROUP BY e.name;
