
NOTE:we have to create two tables Student.db_sqlite3 tand Employee.db_sqlite3
____________________________________________________________________________________________________________________________



Retrieving data from a table - Part I
In this reference, you will learn about different ways to retrieve data from a table.

We use the WHERE keyword to specify different condition(s), using which the dbms filters the records and returns only the records which satisfy the given condition(s).

# Using WHERE clause
To fetch records with an attribute cloumn1 value greater than the given value we write SQL query with the below syntax.

# Syntax
SELECT column1, column2, ..., columnN FROM table_name WHERE column1 > {value}
SELECT * FROM table_name WHERE column1 > {value}
# Example
sqlite> SELECT * FROM Student WHERE score > 35;
The above SQL query returns all the records from Student table which have score greater than 35.

# Result
1|Maude Vanhorne|23|89
2|Sarah Kirwan|34|44
4|Jesse Couch|34|62
5|Israel Gilliland|38|77
6|Michael Aguas|34|87
7|Stephen Boone|25|39
.....
# Try it yourself
Write an SQL query to fetch all the records from Employee table which have age greater than 39
# Expected Output
 13|Elizabeth|Hernandez|40|56119
 98|Joann|Molacek|40|39068
 148|Jolene|Fancher|40|29400
 208|Charlotte|Dorfman|40|48087
 278|Allan|Black|40|28209
 ......
Write an SQL query to fetch all the records from Employee table which have salary greater than 35000
# Expected Output
1|Pat|Friel|23|95708
3|Ellie|Webb|36|56476
4|Heather|Camp|36|91575
5|Retha|Higgins|33|38930
....

Similary, you can use other comparison operators (<, >=, <=, =, <>) to filter the records based on the requirements.

# Try other operators
Write an SQL query to fetch all the records from Employee table which have age less than 25
Write an SQL query to fetch all the records from Employee table which have salary less than 29000
Write an SQL query to fetch all the records from Employee table which have age greater than or equal to 34
Write an SQL query to fetch all the records from Employee table where salary is greater than or equal to 31000
Write an SQL query to fetch all the records from Employee table where salary is less than or equal to 37000
Write an SQL query to fetch all the records from Employee table where age is less than or equal to 19
Write a SQL query to fetch all the records from Employee table which have age equal to 19
# Expected Output
40|Julie|Jackson|19|20351
41|James|Barlow|19|58654
86|Annette|Myers|19|32892
102|Jacklyn|Galeana|19|95691
113|Alex|Khan|19|20052
....
Write a SQL query to fetch the records from Employee table which have salary is equal to 32892
# Expected Output
86|Annette|Myers|19|32892
Write a SQL query to fetch the records from Employee table which have age not equal to 29
# Expected Output
```
1|Pat|Friel|23|95708
3|Ellie|Webb|36|56476
4|Heather|Camp|36|91575
5|Retha|Higgins|33|38930
6|Terry|Blevins|36|32187
......
```
Write a SQL query to fetch the records from Employee table which have salary is not equal to 27000
# Expected Output
```
1|Pat|Friel|23|95708
2|Kimberli|Bostrom|29|20181
3|Ellie|Webb|36|56476
4|Heather|Camp|36|91575
5|Retha|Higgins|33|38930
........
```     
