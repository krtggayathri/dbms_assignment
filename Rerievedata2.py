Retrieving data from a table - Part II
In this reference, you will learn about the equality, inequality and the IN operators.

# Equality, Inequality
To fetch records with an attribute cloumn1 whose value is equal to the given value, we write the below SQL query.

# Syntax
SELECT column1, column2, ..., columnN FROM table_name WHERE column1 = {value}
# Example
sqlite> SELECT * FROM Student WHERE name = "Eva Calhoun";
Above SQL query returns all the records from Student table which have the attribute name equal to "Eva Calhoun".

# Result
92|Eva Calhoun|20|27
As there is only one student with name "Eva Calhoun", we got only one result. The number of rows in the result depends up on the number of rows that match the given condition.
# Try it yourself
Write an SQL query to fetch all the records from Employee table that have age equal to 19.
# Expected Output
40|Julie|Jackson|19|20351
41|James|Barlow|19|58654
86|Annette|Myers|19|32892
102|Jacklyn|Galeana|19|95691
113|Alex|Khan|19|20052
....

Write an SQL query to fetch the records from Employee table which have a salary of 32892.
# Expected Output
86|Annette|Myers|19|32892

Similarly, to fetch records with an attribute cloumn1 whose value is 'not equal to' the given value, we write the below SQL query.

# Syntax
SELECT column1, column2, ..., columnN FROM table_name WHERE column1 != {value}
We can use one of the below syntax for not equal to

!=
<>
# Try it yourself
Write an SQL query to fetch the records from Employee table which have age not equal to 29.
# Expected Output
```
1|Pat|Friel|23|95708
3|Ellie|Webb|36|56476
4|Heather|Camp|36|91575
5|Retha|Higgins|33|38930
6|Terry|Blevins|36|32187
......
```  
Write an SQL query to fetch the records from Employee table which have salary is not equal to 27000.
# Expected Output
```
1|Pat|Friel|23|95708
2|Kimberli|Bostrom|29|20181
3|Ellie|Webb|36|56476
4|Heather|Camp|36|91575
5|Retha|Higgins|33|38930
........
```  
# IN Operator
To fetch the records with an attribute cloumn1 whose value is in the given list of values, we write the below SQL query.

# Syntax
SELECT column1, column2, ..., columnN FROM table_name WHERE column1 IN {values}
# Example
sqlite> SELECT name FROM Student WHERE score IN [52, 90, 99, 18];
Above query returns all the records from Student table which have score equal to one of the scores in the given list i.e [52, 90, 99, 18].

# Result
Cynthia Jones
Maryann Laverriere
Virginia Mcnabb
Robert Norris
William Thompson
Elvira Schmidt
Victoria Lewis
# Try it yourself
Write a SQL query to get salaries of employees from Employee table which have id in [1, 88, 44].
# Expected Output
 95708
 54357
 51285
Write a SQL query to get all records from Employee table which have salary in [25327, 77822]
# Expected Output
 214|Alberta|Williamson|30|77822
 495|Tracy|Fredette|37|25327
# BETWEEN Operator
To fetch records with an attribute cloumn1 value between a given range.

Difference between IN and BETWEEN is that IN check if an attribute value is in a given list of values. Where as in BETWEEN we specify a range (lower and upper limit)
# Syntax
SELECT column1, column2, ..., columnN FROM table_name WHERE column1 BETWEEN ({value1}, {value2})
The lower (value1) and upper(value2) limits are included during comparision
# Example
sqlite> SELECT name FROM Student WHERE score BETWEEN (50, 80);
Above query returns all the records from Student table which have score between 50 to 80 (both inclusive i.e recording having score equal to 50 and 80 are also included).

# Try it yourself
Write an SQL query to fetch all the records in Employee table which have salary between 30000, 50000 (both inclusive)
Write an SQL query to fetch all the records in Employee table which have age between 20, 30 (both inclusive)
