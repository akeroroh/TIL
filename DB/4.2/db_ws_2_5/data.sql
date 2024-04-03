SELECT d.name AS department, e.name AS oldest_employee, max(e.age), avg(e.age)
FROM departments d
INNER JOIN employees e ON e.departmentId = d.id
GROUP BY d.name;

SELECT d.name AS department, e.name AS highest_paid_employee, max(salary) AS max_salary
FROM departments d
INNER JOIN employees e ON e.departmentId = d.id
GROUP BY d.name;

SELECT d.name AS department, 
  CASE WHEN age <= 30 THEN '30세 이하'
    WHEN age BETWEEN 30 AND 40 THEN '30~40세 사이'
    WHEN age >= 40 THEN '40세 이상'
  END AS age_group,
  count()
FROM departments d
INNER JOIN employees e ON e.departmentId = d.id
GROUP BY d.name, age_group;

SELECT d.name AS department, AVG(e.salary) AS avg_salary_excluding_highest
FROM departments d
INNER JOIN employees e ON e.departmentId = d.id
WHERE e.salary < (SELECT MAX(salary) FROM employees WHERE departmentId = d.id)
GROUP BY d.id, d.name;