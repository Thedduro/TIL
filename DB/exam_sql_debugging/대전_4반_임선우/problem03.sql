-- Employees 테이블에서 각 직원의 이름(name)과 직급(position)을 "이름 (직급)"형식으로 합쳐서 'employee_info'라는 별칭의 컬럼으로 조회하는 쿼리를 작성하시오. 
-- (예: '이영준 (CEO)')

SELECT CONCAT(name, ' ', '(', position, ')') AS employee_info
FROM employees;
