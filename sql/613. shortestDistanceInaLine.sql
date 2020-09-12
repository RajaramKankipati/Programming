
drop table point;
CREATE TABLE  point (x INT NOT NULL);
Truncate table point
insert into point (x) values ('-1')
insert into point (x) values ('0')
insert into point (x) values ('2')



---Taking the same table two times for comparing each value
select min(ABS(a.x - b.x)) as shortest from point as a, point as b where a.x <> b.x;

-- Write your MySQL query statement below
select min(ABS(a.x - b.x)) as shortest from point as a left join point as b on a.x <> b.x

---Left join is 5 times faster than using the two tables