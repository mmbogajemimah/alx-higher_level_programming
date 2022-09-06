-- a script that removes all records with a score <= 5 in the table second_table
SELECT score,name
FROM second_table
WHERE score > 5
ORDER BY score DESC;
