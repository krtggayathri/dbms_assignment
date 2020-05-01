Aggregations
In this reference you will learn how to use SQL Aggregation functions on existing database

# What is an Aggregation?
In database management, an aggregation function is a function where the values of multiple rows are grouped together as input on certain criteria to form a single value of more significant meaning.

Below are different common aggregation functions in SQL

AVG: Used to calculate average of all the values in a column
COUNT: Used to count the number of rows
MAX: Used to fetch the max value in a column
MIN: Used to fetch the min value in a column
SUM: Used to calculate sum of all the values in a column
# Aggregation Function in SQL Query
It is used to calculate the average of particular field value of a Table

# Syntax
SELECT AVG(COLUMN_FIELD) FROM TABLE
# Example
sqlite> SELECT AVG(Score) FROM Student;
The above SQL query returns the average of scores of all the records in Student table.

# Result
AVG(Score)
49.11
# Try it yourself
Write an SQL query to calculate the average age of all the Employees in the database.
# Result
```
AVG(age)
29.016
```
Write an SQL query to calculate the average salary of all the Employees in the database.
# Result
```
AVG(salary)
59435.658
```
# Aggregations on selected rows
You can perform aggregation functions on selected rows in a table.

# Syntax
SELECT AVG(COLUMN_FIELD) FROM TABLE WHERE [CONDITION]
# Example
SELECT AVG(AGE) FROM Student WHERE AGE > 21;
# Result
AVG(AGE)
30.4939759036145
The above SQL query returns the average age of all the records in Student table which have age > 21.

# Try it yourself I
Write an SQL query to calculate the average salary of all the employees whose age is greater than 23

Result

AVG(salary)
59565.1643835616
Write an SQL query to calculate the average age of employees whose salary is less than 32000

Result

AVG(age)
28.987922705314
# Aliasing
You can specify an alternative name to an attribute or for an aggregation using AS Keyword.

# Syntax
SELECT AVG(COLUMN_FIELD) AS NEW_FIELD_NAME FROM TABLE
# Example
sqlite> SELECT AVG(AGE) AS average_age_of_students FROM Student;
# Result
average_age_of_students
28.63
Here you can observe that above result is showing average_age_of_students instead of AVG(AGE).

# Try it yourself
Write an SQL query to calculate the average age of employees and alias it with average_age_of_employees

Result

average_age_of_employees
29.016
Write an SQL query to calculate the average salary of employees and alias it with average_salary_of_employees

Result

average_salary_of_employees
59435.658
# Other Aggregation Functions
Similarly you can perform other aggregation operations (COUNT, SUM, MAX, MIN) as well.

# SUM: Try it yourself
Write an SQL query to calculate the sum of all employee's salary

Result

SUM(salary)
29717829
Write an SQL query to calculate the sum of all employee's age

Result

SUM(age)
14508
Write an SQL query to calculate the sum of all employee's salary where employee age is greater than 33

Result

SUM(salary)
9135211
Write an SQL query to calculate the sum of employee's salary and the resultant field name is sum_of_salary_of_employees

Result

sum_of_salary_of_employees
29717829
# MAX: Try it yourself
Write an SQL query to calculate the maximum age of employees

Result

MAX(age)
40
Write an SQL query to calculate the maximum salary of employees

Result

MAX(salary)
99894
Write a SQL Query to calculate the maximum salary of employees where employee age is less than 21

Result

MAX(salary)
99894
Write a SQL Query to calculate out the maximum age of employees where employee salary is greater than 22000

Result

MAX(age)
40
Write an SQL query to calculate the maximum age of employees and the resultant field name is maximum_age_of_employees

Result

maximum_age_of_employees
40
# MIN: Try it yourself
Write an SQL query to calculate the minimum age of among all the employees

Result

MIN(age)
18
Write an SQL query to calculate the minimum salary of among all the employees

Result

MIN(salary)
20052
Write a SQL Query to calculate the minimum salary of all the employees whose age is less than 22

Result

MIN(salary)
20052
Write a SQL Query to calculate the minimum age of all the employees whose salary is greater than 30000

Result

MIN(age)
18
Write an SQL query to calculate the minimum age of employees and alias the result with minimum_age_of_employees

Result

minimum_age_of_employees
18
# COUNT: Try it yourself
Write a SQL Query to calculate the total number of employees in the database.

Result

COUNT(ID)
500
Write a SQL Query to calculate the number of employees whose salary greater than 34000

Result

COUNT(ID)
397
Write a SQL Query to calculate the number of employees whose age greater than 34

Result

COUNT(ID)
132
Write an SQL query to calculate the total number of employees in the database and alias with no_of_employees_count

Result

no_of_employees_count
500
# Quick Reference For SQL Queries
You can refer to SQL syntax in the below cheastsheet

SQL Cheatsheet
