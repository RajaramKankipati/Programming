Drop table orders
Create table orders (order_number int, customer_number int, order_date date, required_date date, shipped_date date, status char(15), comment char(200), primary key(order_number))
Truncate table orders
insert into orders (order_number, customer_number) values ('1', '1')
insert into orders (order_number, customer_number) values ('2', '2')
insert into orders (order_number, customer_number) values ('3', '3')
insert into orders (order_number, customer_number) values ('4', '3')


select customer_number 
from orders 
group by customer_number 
order by count(*) DESC
limit 1;