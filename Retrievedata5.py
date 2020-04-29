Retrieving data from a table - Part V
In this reference, you will learn

How to order the results of a SQL query
How to limit the results
How to remove duplicates from results
# Ordering Results
ORDER BY is used to specify the order of the SQL query result. To order the results in ascending order ASC based on a particular column column1. We write the below SQL query.

# Syntax
SELECT column1, column2, .. columnN  FROM table_name  [WHERE condition]  ORDER BY column1 ASC;
# Example
sqlite> SELECT name, age from Student WHERE age > 21 ORDER BY age ASC;
Above query will fetch name and age attributes of, all the records from Student table which have age > 21 and if you notice the results are in ascending order of age.

# Result
    Scott Coffin|22
    Marjorie Dolejsi|22
    Herman Tucker|22
    Jennie Daniels|22
    Robert Norris|22
    Tena Bierman|22
    Maude Vanhorne|23
    Barbara Wolfe|23
    ....
# Try it yourself
Write an SQL query to fetch last_name, age and salary of all the records from Employee table in ascending order of age
# Expected Output
 Sutter|18|21965
 Rosales|18|25345
 Emberton|18|29984
 Demond|18|32605
 Carrier|18|48916
 ......   
Write an SQL query to fetch all the records from Employee which have age > 21 and the results should be in the ascending order of age .
# Expected Output
    ```
    15|Joseph|Mcdonald|22|41335
    39|Jolene|Barraza|22|24475
    94|Felix|Christensen|22|95712
    110|Alex|Rolan|22|99522
    112|Julie|Vail|22|37880
    .......
    ```
Similar we use DESC instead of ASC to indicate descending order.

# Try it yourself
Write an SQL query to fetch age and salary of all the records from Employee table in the descending order of first_name
# Expected Output
 36|47019
 27|71485
 31|58791
 29|65567
 21|34215
 .....
Write an SQL query to fetch first_name and salary of all the records from Employee table in descending order of age
# Expected Output
 Elizabeth|56119
 Joann|39068
 Jolene|29400
 Charlotte|48087
 Allan|28209
 ......
# Using both ASC and DESC
You can specify more than one field to ORDER BY.

# Syntax
SELECT column1, column2, .. columnN FROM table_name[WHERE condition] ORDER BY column1 ASC/DESC, cloumn2 ASC/DESC;
# Example
sqlite> SELECT name, age from Student WHERE age > 21 ORDER BY age ASC, name DESC;
The above query will fetch name and age of all the records from Student table which have age > 21 and in descending order order age and in ascending order name

i.e the result will have the record in the ascending order of age. If two record have same age then the relative ordering of these two record will in descending order of name.

# Result
Tena Bierman|22
Scott Coffin|22
Robert Norris|22
Marjorie Dolejsi|22
Jennie Daniels|22
Herman Tucker|22
...
# Try it yourself
Write a query to fetch records from Employee table where age>30 in descending order of employee age, first_name
# Expected Output
 170|Stephane|Aguilar|18|66021
 456|Robert|Martin|18|67170
 95|Raymond|Rosales|18|25345
 393|Pamela|Demond|18|32605
 154|Neil|Curtis|18|80063
 67|Mildred|Elliott|18|82213
# Pagination
In this section, you will learn how to limit the number of results of a SQL query. We use OFFSET and LIMIT for this purpose.

OFFSET: Used to specify the position from which you would like to fetch rows.
LIMIT: Used to specify the number of records you would like to have in result.
If there are 100 rows in a table. Specify OFFSET 10 and LIMIT 5 implies that you are requesting for 5 records from 10th row of 100 rows in the table.

# Syntax
LIMIT
SELECT column1, column2, columnN  FROM table_name LIMIT [no of rows]
LIMIT and OFFSET
SELECT column1, column2, columnN  FROM table_name LIMIT [no of rows] OFFSET [row num]
# Example
sqlite> SELECT name, age, score from Student Limit 4 OFFSET 3;
# Result
Jesse Couch|34|62
Israel Gilliland|38|77
Michael Aguas|34|87
Stephen Boone|25|39
# Try it yourself
Write a query to get all records from Employee table from row 5 to 15
# Expected Output
 7|Jeanette|Jennings|31|76580
 8|Jack|Calloway|27|52144
 9|Donald|Tone|37|79912
 10|Brian|Kinghorn|21|48256
 11|Eric|Shipp|21|91210
 12|Helen|Allen|38|93456
 13|Elizabeth|Hernandez|40|56119
 14|Robert|Nelson|34|29376
 15|Joseph|Mcdonald|22|41335
Write a query to select first 10 records from Employee table
# Expected Output
 1|Pat|Friel|23|95708
 2|Kimberli|Bostrom|29|20181
 3|Ellie|Webb|36|56476
 4|Heather|Camp|36|91575
 5|Retha|Higgins|33|38930
 6|Terry|Blevins|36|32187
 7|Jeanette|Jennings|31|76580
 8|Jack|Calloway|27|52144
 9|Donald|Tone|37|79912
 10|Brian|Kinghorn|21|4825
# Distinct
DISTINCT is used to return only distinct i.e unique values.

# Syntax
SELECT DISTINCT column1 FROM table_name WHERE [condition]
# Example
sqlite> SELECT DISTINCT age FROM Student;
The above SQL query will return distinct age of students from Student table.

# Result
23
34
40
38
25
24
.....

Try executing the same SQL query without DISTINCT keyword, you will find that the result will have duplicate values for age.

# Try it yourself
Write an SQL query to fetch unique first_name from Employee table
# Expected Output
 Pat
 Kimberli
 Ellie
 Heather
 Retha
 Terry
 Jeanette
 Jack
 Donald
 .....
