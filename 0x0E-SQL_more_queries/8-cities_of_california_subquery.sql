-- a script that lists all the cities of California that can be found in the database
-- Lists all the cities of `California` state
-- that can be found in the database `hbtn_0d_usa`.
SELECT id, name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = 'California'
    );
