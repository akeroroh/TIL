SELECT avg(age) AS averate_age FROM users;

SELECT country, count() AS user_count FROM users
GROUP BY country;

SELECT * FROM users
ORDER BY balance DESC
LIMIT 1;

SELECT country, avg(balance) FROM users
GROUP BY country;

SELECT max(balance)-min(balance) AS balance_difference FROM users;