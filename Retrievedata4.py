Retrieving data from a table - Part IV (Multiple Conditions)
In this section we will learn how to specify more than one condition to filter rows. We use AND and OR keywords for this purpose.

# AND
To fetch records which satisfy two or more conditions we use AND as mentioned below.

# Syntax
SELECT column1, column2, columnN FROM table_name WHERE [condition1] AND [condition2] AND [condition3]...;
The result for above SQL query will be the records which satisfy all the mentioned conditions i.e condition1, condition2, condition3 ... etc.,

# Example
sqlite> SELECT * from Student WHERE score>80 AND age<40;
The above SQL query returns all the records from Student table which have score > 80 and also age < 40.

# Result
Maude Vanhorne
Michael Aguas
Glenda Villanova
Mazie Corradino
Cynthia Jones
Lori Maldonado
....
# Try it yourself
Write an SQL query to fetch first_name, last_name of all the records from Employee table which have salary> 30000 and salary<35000
# Expected Output
Terry|Blevins
Gabriel|Allen
Steve|Clark
Earl|Klapper
Jack|Smith
Howard|Talley
....
Write an SQL query to fetch all the records from Employee table which have age>35 and salary>99000
# Expected Output
 155|Wade|Bath|36|99862
# OR
To fetch records which satisfy atleast one of the given conditions we use OR. Using OR is same as AND.

# Example
sqlite> SELECT name FROM Student WHERE score>80 or age<20;
# Result
Maude Vanhorne
Michael Aguas
Noel Hurse
Cynthia Mccusker
Glenda Villanova
Mazie Corradino
Cynthia Jones
Lori Maldonado
...
# Try it yourself
Write an SQL query to fetch first_name of all the records from Employee table where salary<44000 or age < 20
# Expected Output
Kimberli
Retha
Terry
Robert
Joseph
Keith
Leonard
Connie
....
Write an SQL query to fetch all the records which have salary > 80000 or age < 35
# Using Both AND & OR
You can use both AND and OR.

Note:
Use bracket appropriately i.e

SELECT * FROM {table_name} WHERE (condition1 AND condition2) OR (condition3 OR condition4) ...
# Try it yourself
Write an SQL query to fetch all records from Employee table which satisfy either one of the below conditions

salary> 30000 and age < 30
salary< 30000 and age > 50
Write an SQL query to fetch all records from Employee table which satisfy both the below conditions

first_name startswith "M" and age < 30
first_name endswith "Y" or first_name endswith A
