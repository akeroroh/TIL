SELECT * FROM users
where first_name LIKE '하%';

SELECT * FROM users
WHERE phone like '%555';

SELECT * FROM users
WHERE country like '경상%';

SELECT * FROM users
WHERE (country like '경%' OR country LIKE '충%')
  and country like '__남%';