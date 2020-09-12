drop table customer
CREATE TABLE customer (id INT,name VARCHAR(25),referee_id INT);
Truncate table customer
insert into customer (id, name, referee_id) values ('1', 'Will', Null)
insert into customer (id, name, referee_id) values ('2', 'Jane', Null)
insert into customer (id, name, referee_id) values ('3', 'Alex', '2')
insert into customer (id, name, referee_id) values ('4', 'Bill', Null)
insert into customer (id, name, referee_id) values ('5', 'Zack', '1')
insert into customer (id, name, referee_id) values ('6', 'Mark', '2')

select name from customer where referee_id is Null or referee_id <> '2' 