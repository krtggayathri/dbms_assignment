One To Many Relationship Using SQL

In this section, we will learn how to implement a One to Many Relationship using SQL.

Before that, let's recollect the concept of Primary Key in a table. A primary key is a column(or a set of columns) in a table that uniquely identifies each row/record in the database table.

Primary keys must contain unique values.
A primary key column cannot have NULL values.
# Foreign Key
A Foreign Key is a column or a combination of columns whose values match the Primary Key in a different table. A Foreign key is used to link two tables together. This is also called as a referencing key.

# Scenario
A customer can create many orders.

# Create customer table with below fields
sqlite> CREATE TABLE Customer(
    customer_id INT PRIMARY KEY,
    name VARCHAR(250),
    mobile_no CHAR(10)
);
# Create records in Customer Table
Insert the below data in the customer table

customer_id	name	mobile_no
1	Yashavant Kanetkar	9912399125
2	David Ascher	8778901256
# Defining One To Many Relationship
Create Order Table:

sqlite> CREATE TABLE Order(
    order_id INT PRIMARY KEY,
    address VARCHAR(250),
    total_price INT,
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
    ); 
FOREIGN KEY(customer_id) REFERENCES Customer(customer_id) implies that customer_id column in Order table should be a value from the list of customer_ids in the Customer table. Note that customer_id is a primary key of the Customer table.

i.e, if database state is as below, then it implies that customer with id=1 has made 2 orders and custoemr with id=2 has made 1 order.

customer_id	name	mobile_no
1	Yashavant Kanetkar	9912399125
2	David Ascher	8778901256
order_id	address	total_price	customer_id
1	Hyderabad	1000	1
2	Kurnool	5000	2
3	Guntur	125	1
# Basic Queries on One To Many Relation
Get the orders details for a given customer id (1)
sqlite> SELECT * FROM BOOK WHERE customer_id =1;
Result
1|Hyderabad|1000|1
3|Guntur|125|1
Get the Order details of customer with id 2
sqlite> SELECT order_id, name, total_price FROM Order WHERE customer_id = 2;
Result
2|Kurnool|5000|2
# Null Values in Table
In SQL, NULL is the term used to represent a missing value. A NULL value in a record(row) represents that the value in the corresponding field is blank (i.e, has NO value). It is very important to understand that a NULL value is different from a zero value or a field that contains empty string (or string with spaces).

In SQL, foreign key supports the NULL value by default.

# Example
Suppose, we are storing Mobile and Owner details in a database. A new mobile is related to an Owner only when he/she buys it.

Mobile:

mobile_id - integer
name - string
price - float
owner_id - Foreign Key
Owner:

owner_id - int
name - string
Create two mobiles (without creating any user). And check the value stored for owner_id in the Mobile table.

# is null Query
You can filter a column with null values using the is null syntax.

sqlite> SELECT * FROM Mobile WHERE owner_id is null; 
The above SQL query returns all the Mobiles which have owner_id field as null.

# Foreign Key with Cascade Delete
A CASCADE is used to specify how DBMS should act upon the deletion of an entry in the parent table. You can make DBMS to delete records in child table when a corresponding entry in the parent table is deleted. To achieve that, a foreign key with ON DELETE CASCADE option is used with CREATE Table statement or an ALTER Table statement.

In the previous example, we haven't mentioned the cascade behavior while creating the Book table. So, deleting Customers shouldn't affect entries in the Book table.

Try deleting all the entries in Customers Table (Don't delete Customers table) and check the entries in the Order table. Order table shouldn't be affected by the delete action on Customer table as we haven't specified CASCADE during table creation.

# Apply on delete Cascade while creating Table
Drop all the tables in the database and create the tables using the below SQL queries.

In Sqlite, to enable on delete cascade foreign key we must configure PRAGMA foreign_keys

sqlite> PRAGMA foreign_keys = on;
After doing that, create a Customer Table

sqlite> CREATE TABLE Customer(
    customer_id INT PRIMARY KEY,
    name VARCHAR(250),
    mobile_no CHAR(10)
);
Create Order Table applying On Delete Cascade

sqlite> CREATE TABLE Order(
    order_id INT PRIMARY KEY,
    address VARCHAR(250),
    total_price INT,
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES Customer(customer_id) ON DELETE CASCADE
    ); 
Create records in both the tables using previously mentioned data. Now, on deleting the rows with customer_id 1, from Customer Table, you will observe that some of the order entries are automatically deleted. This is because of the CASCADE option.

# Try it yourself
Create a Student table with the following fields
Q1:

student_id - int, primary key
name - varchar(250)
email - varchar(250)
Create a Project table with following fields
INSERT INTO Student2(student_id,name,email) values(3,'vani','vani@gmail.com');
project_id - int , primary key
title - varchar(250)
Write an SQL Query to create Student and Project tables and establish the One To Many Relationship between them.
Q1:CREATE TABLE Project(project_id INT PRIMARY KEY,title VARCHAR(200),student_id INT,FOREIGN KEY(student_id) REFERENCES Student2(

Write an SQL Query to insert the below data into respective tables.

Student

student_id	name	email
1	Ramu	ramu@gmail.com
2	Latha	latha@gmail.com
3	Raju	raju@gmail.com
4	Laxman	laxman@gmail.com
Project

project_id	title	student_id
1	Android Task Monitoring	1
2	Online Mobile Recharge Portal Project	2
3	Detecting E Banking Phishing Websites Using Associative Classification	1
4	Vehicle Tracking Using Driver Mobile Gps Tracking	2
5	Sentiment Analysis for Product Rating	3
6	Fingerprint Based ATM System	4
Write an SQL Query to get Project details of the student with id 2.

Delete a student record in the Student table and you should find that all his/her projects are also deleted from Project table.

Delete a project and it shouldn't effect any of the students rows.




CREATE TABLE Project(project_id INT PRIMARY KEY,title VARCHAR(200),student_id INT,FOREIGN KEY(student_id) REFERENCES Student2(

DELETE FROM Customer1 WHERE customer_id=1;
sqlite> SELECT * FROM Customer1;
2|bhanu|56378994
sqlite> SELECT * FROM Order1;
1|hyderabad|2000|1
2|kurnool|1000|2
3|guntur|125|1


INSERT INTO Student2(student_id,name,email) values(3,'vani','vani@gmail.com');
sqlite> INSERT INTO Student2(student_id,name,email) values(4,'laxi','laxi@gmail.com');
sqlite> SELECT * FROM Student2;
1|gay|gayi@gmail.com
2|rama|rama@gmail.com
3|vani|vani@gmail.com
4|laxi|laxi@gmail.com
sqlite> DELETE FROM Student2 WHERE student_id=1;
sqlite> SELECT * FROM Student2;
2|rama|rama@gmail.com
3|vani|vani@gmail.com
4|laxi|laxi@gmail.com
sqlite> SELECT * FROM project;
1|android project|1
2|mobile recharge|2
3|bank project|1
4|vehicle|2
5|sentiment|3
6|finger_print|4
sqlite> DELETE FROM project WHERE student_id=2;                                                                                 
sqlite> SELECT * FROM project;
1|android project|1
3|bank project|1
5|sentiment|3
6|finger_print|4
sqlite> SELECT * FROM Student2;
2|rama|rama@gmail.com
3|vani|vani@gmail.com
4|laxi|laxi@gmail.com
sqlite> SELECT * FROM Student2;





