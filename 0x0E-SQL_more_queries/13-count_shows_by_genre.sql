-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
--- SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
--- FROM tv_genres RIGHT JOIN tv_show_genres
--- ON tv_genres.id = tv_show_genres.genre_id
--- GROUP BY genre
--- ORDER BY number_of_shows DESC;
SELECT tv_genres.name AS 'genre',, COUNT(*) AS 'number_of_shows' from tv_genres INNER join tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;