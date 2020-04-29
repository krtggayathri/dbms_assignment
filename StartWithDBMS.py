Getting Started with SQL

In this reference, you will learn how to perform basic operations on a database.

# Creating a database
# Syntax
$ sqlite3 {database_name}
# Example
$ sqlite3 db.sqlite3
After executing the above command i.e., sqlite3 db.sqlite3 you should be able to see db.sqlite3 file in your current working directory. Check if it is created by executing the below command.

$ ls
...
db.sqlite3
...
# SQLite Prompt
We run all our SQL and database related commands in sqlite prompt/shell.

$ sqlite3 db.sqlite3  # Type this
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite>
sqlite3 db.sqlite3 opens an sqlite shell/prompt i.e., sqlite>. You can execute all queries on the db.sqlite3 database from this prompt.

# List all tables in a database
To get the list of tables in a database, we use the below command.

$ sqlite3 db.sqlite3  # Type this
sqlite> .tables
Executing .tables inside the sqlite shell should list all the tables in db.sqlite3 database.

As we haven't created any table in the database yet, we can't see any tables.

# Creating a table
Let's create a table in our database.

# Syntax
CREATE TABLE {table_name}(column1 type, column2 type, ..);
# Example
sqlite> CREATE TABLE user(id INT);
On executing the above sql query in your sqlite prompt a user table with id column (which takes integer values) is created.

You can also check the schema of the Student table.

sqlite> .schema user
CREATE TABLE user(id INT);
.schema gives you the sql query needed to create the table.

Commonly used fields types

VARCHAR - For Strings
INT - For Integers
DATE - For date (stored in YYYY-MM-DD format)
Time - For time (stored in HH:MI:SS format)
DATETIME - For date-time (stored in YYYY-MM-DD HH:MI:SS format)
BOOLEAN - For boolean values
FLOAT - For float values
# Try it yourself
Create a table Mobile with the following fields
name - VARCHAR(200)
price - FLOAT
Now try executing .tables command to see the table you have just created.

sqlite> .tables
...
Mobile
...
# Creating a table with Primary Key
# Syntax
CREATE TABLE {table_name}(ID INT PRIMARY KEY NOT NULL , column1 type, column2 type, ..);
# Explanation
A primary key is a field in a database table which uniquely identifies each row/record in the table.

Primary keys must contain unique values.
A primary key column can not have NULL values.
A table can have only one primary key.
# Example
sqlite> CREATE TABLE Student (ID INT PRIMARY KEY NOT NULL, NAME VARCHAR(250), AGE INT,SCORE INT);
# Try it yourself
Create a table Book with the following fields
name - VARCHAR(200)
id - INT - PRIMARY KEY
price - FLOAT
# Insert data into table
# Syntax
INSERT INTO {table_name}(column1, column2, column3,...columnN) VALUES (value1, value2, value3,...valueN);
# Example
sqlite> INSERT INTO Student(id, name, score, age) values(1, 'Ram', 100, 20);
Above SQL query creates a row in the student table with id - '1', name - 'Ram', score - '100' and age - 20.

# Try it yourself
Insert the following Book data.

"Harry Potter" book with id as 1 and price = 2000
"Detective Pikachu" book with id as 2 and price = 3000
"Jungle Book" book with id as 3 and price = 5000
Insert the following Mobile data

'Galaxy Note 10' with price = 30000
'iPhone 11 Pro' with price = 40000
# Result
You can check result by using select statement which we will learn next.

# Get data from table
We use SELECT query to fetch the data from a table.

# Syntax
SELECT * FROM {table_name}
# Example
sqlite> SELECT * FROM Student;
# Result
1|Ram|100|20
# Try it yourself
Get data from Book table
# Expected Output
Harry Potter|1|2000.0
Detective Pikachu|2|3000.0
Jungle Book|3|5000.0
Get data from Mobile table
# Expected Output
Galaxy Note 10|30000
iPhone 11 Pro|40000
# Update existing rows
We use UPDATE keyword to update existing rows in a table.

# Syntax
UPDATE table_name SET column1 = value1;
# Example
sqlite> UPDATE Student SET name = "Lakshman";
The UPDATE keyword, when used in the above mentioned way, updates the value for all the existing rows in the table.

# Try it yourself
Update name field in Book table to 'War and Peace'
Use the SELECT query you have learnt in the previous section to check if the data in Book table is updated correctly.
# Expected Output
War and Peace|1|2000.0
War and Peace|2|3000.0
War and Peace|3|5000.0
Update price field in Mobile table to 10000
Use the SELECT query you have learnt in the previous section to check if the data in Mobile table is updated correctly.
# Expected Output
Galaxy Note 10  |10000
iPhone 11 Pro   |10000
# Update multiple columns
You can also update more than one column in a single UPDATE query.

# Syntax
UPDATE table_name SET column1 = value1, column2 = value2,...., columnN = valueN;
# Example
sqlite> UPDATE Student SET name = "Ram", score = 100;
# Try it yourself
Update name field to 'The Secret' and price to 50000 in Book table
Use the SELECT query you have learnt in the previous section to check if the data in Book table is updated correctly.
# Expected Output
The Secret|1|50000.0
The Secret|2|50000.0
The Secret|3|50000.0
Update name field to 'realme' and price to 90000 in Mobile table
Use the SELECT query you have learnt in the previous section to check if the data in Mobile table is updated correctly.
# Expected Output
90000|realme
90000|realme
# Update only selected rows
You can also specify conditions to update only selected rows in a table.

Where keyword is used to specify conditions.

# Syntax
UPDATE table_name SET column1 = value1, column2 = value2,...., columnN = valueN WHERE condition;
# Example
sqlite> UPDATE Student SET name = "Ram", score = 95 WHERE id = 1;
# Try it yourself
Update name field to 'War' in book table where id=1
Use the SELECT query you have learnt in the previous section to check if the data in Book table is updated correctly.
# Expected Output
War|1|50000.0
The Secret|2|50000.0
The Secret|3|50000.0
Update price field to 200000 in Mobile table where name='realme'
Use the SELECT query you have learnt in the previous section to check if the data in Mobile table is updated correctly.
# Expected Output
200000|realme
200000|realme
In the above example, as both the rows satisfy the condition, price of both the rows is updated.

# Delete a row in table
DELETE keyword is used to delete existing records from a table.

# Syntax
DELETE FROM {table_name} WHERE {condition};
# Example
sqlite> DELETE from Student where score=99;
Above query deletes all the rows in Student table which have score=99.

# Try it yourself
Delete records in Book table where name='War'
Use the SELECT query you have learnt in the previous section to check if the data in Book table is updated correctly.
# Expected Output
The Secret|2|50000.0
The Secret|3|50000.0
Delete records in Mobile table where price=200000
Use the SELECT query you have learnt in the previous section to check if the data in Mobile table is updated correctly.
# Expected Output
In the above example, as all the rows in Mobile table satisfy the condition, we get an empty list.

# Delete a table in database
# Syntax
DROP TABLE table_name
DROP TABLE statement deletes table.

# Example
sqlite> DROP TABLE student;
# Try it yourself
Delete Book table
Delete Mobile table
You can use .tables to check if the tables are deleted

# Create table with AUTOINCREMENT
# Syntax
CREATE TABLE {table_name}(column1 type PRIMARY KEY NOT NULL AUTOINCREMENT, column2 type, column3 type, ..);
AUTOINCREMENT allows a unique number to be generated automatically when a new record is inserted into a table.

Often this is the primary key field that we would like to be created automatically every time a new record is inserted.
By default, the starting value for AUTO_INCREMENT is 1, and it will increment by 1 for each new record created.
# Example
sqlite> CREATE TABLE People (ID INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT, NAME VARCHAR(250), AGE INT);
# Insert data into People table
# Example
sqlite> INSERT INTO People(name, age) values('Hernandez',20);
Above SQL query creates a row in the People table with id - '1', name - 'Hernandez' and age - 20. Use select query to fetch the entries in People table and check the id for Hernandez

Insert another row

sqlite> INSERT INTO People(name, age)values('Ronald',30);
Above SQL query creates a row in the People table with id - '2', name - 'Ronald' and age - 20. Use select query to fetch the entries in People table and check the id for Ronald

