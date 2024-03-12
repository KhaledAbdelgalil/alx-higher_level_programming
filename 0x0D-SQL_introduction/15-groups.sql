-- GROUB by score
SELECT score, COUNT(id) AS number FROM second_table GROUP BY score DESC;
