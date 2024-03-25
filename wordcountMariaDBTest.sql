--------------------------------------------------------------------------------
-- wordcountMariaDBTest.sql                                                   --
--------------------------------------------------------------------------------

-- Open MariaDB and enter your password
-- Run command: source .\..\..\wikipedia-dataset\wordcountMariaDBTest.sql

-- Set timeout to 600 seconds (10 minutes)
SET GLOBAL innodb_lock_wait_timeout = 600;
SET innodb_lock_wait_timeout = 600;

CREATE DATABASE wikipedia;

USE wikipedia;

-- Start time.
SELECT
    NOW();

-- Load words from input.txt into a table called "words".
CREATE TABLE words (word varchar(20));

LOAD DATA LOCAL INFILE './../../wikipedia-dataset/wikipedia-subset.xml'
INTO TABLE words
LINES TERMINATED BY ' ';

-- SQL Query to create a table called "top_words"
-- for the three most frequently used words.
CREATE TABLE top_words AS (
    SELECT
        word,
        COUNT(*) as frequency
    FROM
        words
    WHERE
        word != ' '
    GROUP BY
        word
    ORDER BY
        frequency DESC
    LIMIT
        3
);

-- Create a view of the "top_words" table.
-- CREATE VIEW top_words_view AS
-- SELECT word, frequency
-- FROM top_words;
-- mariadb-show top_words;
SELECT
    *
FROM
    top_words;

-- Stop time.
SELECT
    NOW();

-- DROP VIEW top_words_view;
DROP TABLE words;

DROP TABLE top_words;

DROP DATABASE wikipedia;
