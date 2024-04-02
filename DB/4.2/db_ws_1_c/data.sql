SELECT genre, count(*) AS count, avg(duration) AS averate_duration FROM songs
GROUP BY genre;