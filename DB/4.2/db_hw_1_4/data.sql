SELECT * FROM tracks
WHERE name LIKE '%love%';

SELECT * FROM tracks
WHERE GenreId = 1 AND Milliseconds >= 300000
ORDER BY UnitPrice DESC;

SELECT GenreId, count() AS TotalTracks FROM tracks
GROUP BY GenreId;

SELECT GenreId, sum(UnitPrice) AS TotalPrice FROM tracks
GROUP BY GenreId
HAVING TotalPrice >= 100;