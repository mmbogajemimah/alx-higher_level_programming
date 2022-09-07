--  a script that creates the table unique_id on your MySQL server.
-- If the table unique_id already exists, your script should not fail

CREATE TABLE IF NOT EXISTS unique_id(
	id INT UNIQUE,
	name VARCHAR(256) NOT NULL);
