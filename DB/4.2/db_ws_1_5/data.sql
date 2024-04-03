select * FROM users
WHERE age >= 30 AND balance > 1000;

SELECT * FROM users
WHERE balance <= 1000 AND age <= 20;

SELECT * FROM users
WHERE first_name like '현%' AND country = '제주특별자치도'
ORDER BY age DESC
LIMIT 1;

SELECT * FROM users
WHERE last_name like '%박' AND age >= 25
ORDER BY age
LIMIT 1;

SELECT * FROM users
WHERE first_name LIKE '재은' or first_name LIKE '영일'
ORDER BY balance DESC
LIMIT 1;

SELECT *, max(balance) AS max_balance FROM users
GROUP BY country
ORDER BY balance DESC;

SELECT * FROM users
WHERE age >= 30
  AND balance > (SELECT avg(balance) FROM users WHERE age >= 30);