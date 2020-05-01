
GROUP BY
Till now you have learnt how to calculate aggregates on all the rows of a table or on a selected rows. In this reference you will learn how split a table in multiple groups and apply aggregation on each group.

# GROUP BY in SQL
The GROUP BY keyword in SQL is used to group rows which have same values for the mentioned attributes. You can perform aggregations on these groups to get finer analytics.

For example with group you can perform operations like

Calculating the average of student scores for each section for the below given model.
Student
    - student_id - integer
    - name - string
    - score - float
    - section - integer
    
# Points to remember
GROUP BY clause is used with the SELECT statement.
If an SQL query has a WHERE clause, the GROUP BY clause is placed after the WHERE clause.
In the query, GROUP BY clause is placed before ORDER BY clause if used any.
GROUP BY returns only one result per group of data.
# Syntax
SELECT column1, aggregate_function(columnx) FROM table_name WHERE condition GROUP BY column1, column2 ....;
Here aggregate_function is one of SUM , AVG, MIN, MAX, COUNT.

# Examples
Get the maximum score of students for each age group.
SELECT AGE, MAX(SCORE) FROM Student GROUP BY AGE;
The above SQL query, segregates the rows in Student table into multiple groups, where each group has rows which have same value for age attribute and calculates max score for each group.

# Result
AGE|MAX(SCORE)
18|95
19|68
20|95
21|97
22|99
23|93
.......
Calculate the number of students having name starting with "a" for each age value in database.
SELECT AGE as student_age, COUNT(ID) as no_of_students FROM Student WHERE name LIKE "a%" Group BY AGE ORDER BY AGE; 

1.PQUERY:Here group the same age students and whose age is greater than 21 and find the number of students using count aggregation.
A:SELECT AGE AS student_age,COUNT(ID) AS no_of_students FROM Student WHERE GROUP BY AGE;
Result

22|6
23|5
24|6
25|8
26|2
27|1
....
Note: Above Example are explained by using the previous student database
# Try it yourself
2.Write an SQL query to calculate the number of employee who are getting same salary for each salary value greater than or equal to 90000
A:SELECT SALARY,COUNT(ID) AS no_of_employees WHERE salary>90000 GROUP BY SALARY;
Result

SALARY|no_of_employees
90267|1
90432|1
90810|1
90818|1
90836|1
90937|1
90986|1
......
3.Write an SQL query to calculate the number of employee who have same age for each age value greater than or equal to 34. Consider students whose first_name is not equal to "Tony". Results should be in the ascending order of employee age. Result
A:qlite> SELECT AGE,COUNT(ID) AS no_of_employees FROM employee  WHERE AGE<=34 AND (NOT first_name="TONY") GROUP BY AGE ORDER BY AGE;
AGE|no_of_employees
18|20
19|24
20|20
21|24
22|22
23|25
24|21
25|20
26|19
......
4.Write an SQL query to calculate the average salary of employees who have the same first_name. Result
A.SELECT FIRST_NAME,SUM(SALARY) AS sum_of_employee_salary FROM employee GROUP BY FIRST_NAME ORDER BY FIRST_NAME;

FIRST_NAME|sum_of_employees_salary
Abraham|91483
Adam|23373
Agnes|71885
Alberta|77822
Alejandro|72011
Alex|196982
Alfred|33326
Allan|57005
Amanda|88058
Amelia|69490
.........
# Having Clause
This is similar to WHERE clause but used to apply conditions on groups.

SELECT age, Count(id) 
FROM Student 
GROUP BY age
HAVING Count(id) > 5; 
The above SQL query, segregates the rows in Student table into multiple groups, where each group has rows which have same value for age attribute and calculates number of id attributes in each group. And the having clause selects only the groups which have count(id) greater than 5.

# Result
AGE|Count(id)
19|6
22|6
24|6
25|8
31|6
34|6
37|7
38|7
# Try it yourself
5.Write an SQL query to calculate average salary of employees for each age value in db, and your SQL query should return entries which have average salary greater than 9000.
A.SELECT FIRST_NAME,SUM(SALARY) AS sum_of_employee_salary FROM employee GROUP BY FIRST_NAME ORDER BY FIRST_NAME;
