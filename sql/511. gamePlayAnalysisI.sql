
DROP TABLE [db].[dbo].[activity];

CREATE TABLE activity
(
    player_id INT NOT NULL, -- primary key column
    device_id INT,
    event_date DATE,
    games_played INT,
    PRIMARY KEY (player_id, event_date)
);

-- Insert rows into table 'activity'
INSERT INTO activity
( -- columns to insert data into
 [player_id], [device_id], [event_date], [games_played]
)
VALUES
(1, 2, '2016-03-01', 5),
(1, 2, '2016-05-02', 6),
(2, 3, '2017-06-25', 1),
(3, 1, '2016-03-02', 0),
(3, 4, '2018-07-03', 5)


-- Select rows from a Table or View 'TableOrViewName' in schema 'SchemaName'
SELECT [player_id]
      ,[device_id]
      ,[event_date]
      ,[games_played]
  FROM activity;


/*
Write your MySQL query statement below
*/
select player_id, min(event_date) as first_login from activity group by player_id