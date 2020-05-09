Using SubQueries in the WHERE Clause

Similar to SELECT clause we can also use SubQueries in WHERE clause. A subquery in a WHERE clause can be used to qualify a column against a set of rows. Below are some scenarios where we should use SubQuery in WHERE clause.

# Scenario - I (Exist and Not Exists)
An EXISTS condition can be used in combination with a subquery. It results in TRUE whenever the subquery returns one or more values else results in FALSE. And a NOT EXISTS condition results in TRUE if zero rows are returned.

# Syntax For EXISTS With Subquery
SELECT column1, column2, column3, ..., columnN 
FROM TABLE 
WHERE EXISTS (sub query); 
# Example
Find the students who didn't register in any course except for course with id equal to 1.

SELECT s.id, s.name, s.age 
FROM Student s 
WHERE EXISTS (
    SELECT e.student_id 
    FROM Enrollment e 
    WHERE s.id=e.student_id AND e.course_id=1
) AND NOT EXISTS (
    SELECT e.student_id 
    FROM Enrollment e 
    WHERE s.id=e.student_id AND e.course_id<>1
);
In the above SQL query we are using two subqueries

(SELECT e.student_id FROM Enrollment e WHERE s.id=e.student_id and e.course_id=1) to find if the user is registered in course 1
(SELECT e.student_id FROM Enrollment e WHERE s.id=e.student_id and e.course_id<>1) to find if the user is not registered for course 2
# Result
id	name	age
7	Cody Spearman	26
26	Charles Edwards	23
# Points to remember
The WHERE clause returns all records where the EXISTS clause is TRUE.
Here EXIST clause uses a correlated subquery. The outer query is correlated to the inner query.
The EXISTS clause returns TRUE if one or more rows are returned by the subquery.
# Try it Yourself
You can try below questions on given student and course database

Write an SQL Query to get the students who didn't register to any course in the year 2015.
# Result
id	name	age
1	Christopher Arwood	22
2	Cathi Tyson	21
3	Tracy Bartlebaugh	28
5	Marilyn Sindelar	30
6	Tom Pippin	25
...	...	...
Write an SQL Query to get the courses to which no student has registered.
# Result
id	name	credits
3	Discrete Structures	4
5	Data Structures and Algorithms Lab	2
6	Computer Architecture	3
7	Operating Systems	3
11	Environmental Studies	1
13	Artificial Intelligence	5
14	Computer Networks	2
...	...	...
# Using SubQueries in the FROM Clause
Similar to SELECT & WHERE clauses we can also use SubQueries in FROM clause

# Scenario - I
One common scenario to use a SubQuery in FROM clause is when we are trying to use an aggregate function on an aggregated result, this is explained in the below scenario.

Let's say you want to find the average score for each student.

SELECT student_id, AVG(score) AS avg_score 
FROM Enrollment 
GROUP BY course_id;
# Result
student_id	avg_score
7	60.6470588235294
6	63.2631578947368
6	61.6153846153846
6	63.2727272727273
4	58.25
...	...
So far, no mystery, right? But what if we want to find maximum of avg_score? Normally, our first approach would be something like that:

SELECT student_id, MAX(AVG(score)) AS max_avg_score 
FROM Enrollment 
GROUP BY student_id;
We will get an error the following error:

Error: misuse of aggregate: AVG()

Makes this problem a perfect example where a sub-query needs to be used. What we need to do is to first generate the field avg_score, so when we use MAX the average of score is already there!

This needs to be done in the FROM clause, as it comes before the filter SELECT clause in the order of execution. Let’s see how this query looks like:

SELECT MAX(avg_score) as max_avg_score
FROM (
-- Here we make our sub-query:
    SELECT student_id,
    AVG(score) AS avg_score
    FROM Enrollment
    GROUP BY course_id
-- End of the sub-query
) AS enroll;
Result

max_avg_score
68.533
Above data is a sample value which can vary on the database you are using
The sub-query in the FROM clause is evaluated first and then the results of the evaluation are stored in a new temporary relation. And then the outer query is evaluated.

# Try it yourself
Write an SQL query to find the sum of average_score for each student where avg score greater than 60.
# Result:
sum(avg_score)
822.548400273841
Write an SQL query to find the min of average_score for each student where avg score less than 60.
# Result:
MIN(avg_score)|
---|
22.0|

# Scenario - II
Another situation to use a subquery in a FROM clause is Joining Derived Tables.

# Example
Find the student, course pairs where student average scores is greater then the course average scores.

SELECT student_averages.student_id, student_averages.student_avg_score, course_averages.course_id, course_averages.course_avg_score 
FROM (
    SELECT student_id, AVG(score) AS student_avg_score 
    FROM Enrollment 
    GROUP BY student_id
) AS student_averages JOIN (
    SELECT course_id, AVG(score) AS course_avg_score 
    FROM Enrollment 
    GROUP BY course_id
) AS course_averages
WHERE student_averages.student_avg_score > course_averages.course_avg_score;
In the above query we have combined two derived tables.

First subquery calculates the student's average score i.e student_avg_score
Second subquery calculates the courses's average score i.e course_avg_score. Both the individual results are joined in FROM clause using JOIN.
# Result
student_id	student_avg_score	course_id	course_avg_score
2	62.75	1	60.6470588235294
2	62.75	3	61.6153846153846
2	62.75	5	58.25
2	62.75	8	54.5294117647059
2	62.75	9	60.0434782608696
2	62.75	11	60.2
2	62.75	12	56.45
2	62.75	15	58.1764705882353
2	62.75	16	55.2307692307692
2	62.75	18	57.5555555555556
2	62.75	19	58.6428571428571
...	...	...	...
# Try it yourself
Write an SQL query to fetch the student_id, no_of_courses, course_id, and no_of_students who are taken at least 3 courses.
# Result
student_id	no_of_courses	course_id	no_of_students
2	4	1	17
2	4	2	19
2	4	3	13
2	4	4	22
2	4	5	12
...	...	...	...
# Key points
A derived table(subquery) must be aliased so that you can reference its results.
# Using Subqueries in the HAVING Clause
HAVING clause is used filter the groups of records generated by using GROUP BY, you can use subqueries in HAVING clause to perform powerful operations.

# Scenario - I
If you want to compare the average of a group to the overall average, then how can we write a query.

Find all the students whose average score is greater than 60.

SELECT student_id, AVG(score) as  avg_score
FROM Enrollment 
GROUP BY student_id 
HAVING AVG(score) > 60;
# Result
student_id	avg_score
2	62.75
3	66.0
5	76.0
6	80.4
9	62.75
...	...
Instead of 60 what if we need all the student ids whose score is greater than average of all the students. An SQL query to achieve this would look like:

SELECT student_id, AVG(score) as avg_score
FROM Enrollment 
GROUP BY student_id 
HAVING AVG(score)>(SELECT AVG(score)
                   FROM Enrollment);
# Result
student_id	avg_score
2	62.75
3	66.0
5	76.0
6	80.4
...	...
# Syntax
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition OPERATOR (SELECT column_name(s)
                           FROM table_name
                           WHERE condition
                           GROUP BY column_name(s))
# Try it yourself
Write an SQL query to fetch student id and average score(`avg_score) for each student having an avg score greater than the average score of all the students.
# Result:
student_id|avg_score 2|7 3|6 5|12 6|8 9|15 ...|...

Above table is filled with dummy data
Write an SQL query to fetch student id and average score(avg_score) for each student whose average score less than the average score of all the students who enrolled in 2015.
# Result:
student_id	score
1	19
2	7
3	6
4	5
5	12
...	...
Above table is filled with dummy data
# Scenario - II
Correlated Subqueries in HAVING clause. subqueries in HAVING clause can be correlated with fields from the outer query.

# Key points
You can use subqueries in HAVING clause to filter out groups of records.
HAVING is very useful in filtering on aggregate values such as averages, summations, and count.
# Things to Keep in Mind
A subquery is just a SELECT statement inside an SQL query.
SubQueries are always enclosed in parenthesis ().
A subquery that returns single value can be used anywhere you would use an expression, such as in a column list or filter expression.
A subquery that returns more than one value is typically used where a list of values, such as those used in and IN operator.
Warning! Subqueries can be very inefficient. If there are more direct means to achieve the same result, such as using an inner join, you’re better for it.
You can nest subqueries up to thirty-two levels deep on the SQL server.
