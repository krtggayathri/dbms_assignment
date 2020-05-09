Joins
# Introduction
In the previous sections, you have learned the importance of organizing data into multiple tables. In this section, you will learn how to write a query to retrieve data which is spread across multiple tables.

# SQL Join
Assume that there are Order and Customer tables. How can you retrieve the details of customers who placed at least two orders?

We use the SQL JOIN operation to query data that is spread across more than one table. There are many different types of SQL JOIN operations, but in practice we will use the INNER JOIN most of the times.

# How INNER JOIN works
In INNER JOIN operation, we specify columns of two tables and a condition that is connecting the two tables. In most of the cases, we use equality of two fields (one in each table) as a condition.

Suppose we are doing an INNER JOIN from table A to table B. Each row in table A is checked against all the rows of table B to see if the pair meets the condition. Each pair of rows which satisfy the condition are stitched together to form a new row in an imaginary table (which doesn't exist in the DB). This new row contains fields from both the tables A and B.

InnerJoin

You can perform any of the SQL queries (including JOIN) you've learnt so far on this imaginary table which has fields from both tables.

# Example
Below tables are used to explain JOIN queries.

sqlite> CREATE TABLE Owner(
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(250)
);

sqlite> CREATE TABLE Car(
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_no VARCHAR(250),
    owner_id INT,
    FOREIGN KEY(owner_id) REFERENCES Owner(owner_id) ON DELETE CASCADE
);
sqlite> INSERT INTO Owner (name) VALUES ("RAM");
sqlite> INSERT INTO Owner (name) VALUES ("John");
sqlite> INSERT INTO Owner (name) VALUES ("Robert");
sqlite> INSERT INTO Owner (name) VALUES ("Mike");
sqlite> INSERT INTO Owner (name) VALUES ("Jessie");

sqlite> INSERT INTO Car (model_no, owner_id) VALUES ("Benz C Class", 1);
sqlite> INSERT INTO Car (model_no, owner_id) VALUES ("Benz D Class", 2);
sqlite> INSERT INTO Car (model_no, owner_id) VALUES ("Benz E Class", 3);
sqlite> INSERT INTO Car (model_no, owner_id) VALUES ("Benz F Class", 3);
sqlite> INSERT INTO Car (model_no, owner_id) VALUES ("Benz G Class", 3);
sqlite> INSERT INTO Car (model_no) VALUES ("BMW");
sqlite> INSERT INTO Car (model_no) VALUES ("Ford");
Owner
owner_id	name
1	RAM
2	John
3	Robert
4	Mike
5	Jessie
Car
car_id	model_no	owner_id
1	Benz C Class	1
2	Benz D Class	2
3	Benz E Class	3
4	Benz F Class	3
5	Benz G Class	3
6	BMW	null
7	Ford	null
# INNER JOIN Syntax
SELECT column_name1, column_name2, column_name3... FROM table1 INNER JOIN table2 ON table1.column1 = table2.column2;
In the above SQL query, INNER JOIN stitches each row in table1 with rows in table2 which satisfy the condition that is stated in the ON clause.

# Example
sqlite> SELECT * FROM Owner INNER JOIN Car on Owner.owner_id==Car.owner_id;
# Result
owner_id	name	car_id	model_no	owner_id
1	RAM	1	Benz C Class	1
2	John	2	Benz D Class	2
3	Robert	3	Benz E Class	3
3	Robert	4	Benz F Class	3
3	Robert	5	Benz G Class	3
# Using join result for further operations
You can treat the joined table just like any other table.

sqlite> SELECT CarWithOwnerDetails.owner_id, CarWithOwnerDetails.name, CarWithOwnerDetails.model_no, CarWithOwnerDetails.car_id FROM (Owner LEFT OUTER JOIN Car) as CarWithOwnerDetails WHERE CarWithOwnerDetails.model_no LIKE "B%";
In the above SQL query we have named the result as T and referred it for further filtering and in SELECT as well.

