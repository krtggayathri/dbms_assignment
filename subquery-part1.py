Introduction to SubQueries

SubQueries are queries which are nested inside other queries. Hence, they are also called as nested queries. A subquery is used to return data that can be used in the main query.

We will use the following tables in examples:

Student (
    id INT PRIMARY KEY, 
    name VARCHAR(250), 
    age INT
 );
 
Course (
    id INT PRIMARY KEY,
    name VARVHAR(250), 
    credits INT
 );
 
Enrollment(
    student_id INT,
    course_id INT,
    score INT,
    year INT,
    semester INT,
    FOREIGN KEY(student_id) REFERENCES Student(id) ON DELETE CASCADE,
    FOREIGN KEY(course_id) REFERENCES Course(id) ON DELETE CASCADE
);
# Scenario
Suppose, we need to retrieve the list of students whose age is greater than the average age of all the students.

A naive way of solving this problem is

Calculate the average age of all the students in the database.
Use the average value calculated in the previous step to filter the student records.
SELECT AVG(age) 
FROM Student;
SELECT id, name, age 
FROM Student 
WHERE age > 23.65;
# Result
id	name	age
3	Tracy Bartlebaugh	28
5	Marilyn Sindelar	30
6	Tom Pippin	25
7	Cody Spearman	26
8	Martha Alexander	27
..	..	..
But, with this kind of solution, every time a new student is created or an existing student's age is updated, we have to execute the first query and update the second query.

The reason for the above problem is that our second query has a fixed value which is not updated dynamically based on the creation of a new student OR updation of a student entry. This problem can be easily solved using subqueries.

# Solution
SELECT id, name, age 
FROM Student 
WHERE age > (
    SELECT AVG(age) 
    FROM Student
);
Here, (SELECT AVG(age) FROM Student) is a subquery. Using a subquery has eliminated the need to calculate the average age of students in a separate query and then plug it into the main query. We let the subquery do the work for us!

Here, average value is calculated on-the-fly; That is, everytime the above SQL Query is executed, the inner subquery is first calculated and then the outer query gets executed. So, the query automatically adjusts itself to data changes in the table.

Subqueries make it possible for you to write queries that are more dynamic and data-driven.

# Result
id	name	age
3	Tracy Bartlebaugh	28
5	Marilyn Sindelar	30
6	Tom Pippin	25
7	Cody Spearman	26
8	Martha Alexander	27
...	...	...
When working with subqueries, the main statement is sometimes referred as the Outer Query. Also, Subqueries are enclosed in parenthesis which makes them easier to spot.

You can use subqueries in the below SQL clauses

SELECT clause
WHERE clause
HAVING clause
FROM clause
# Using Subqueries in the SELECT Clause
SELECT statement is used to select the columns to retrieve data from or to evaluate an expression to a single value.

A subquery which is used in the SELECT clause should return a single value. In this case, you can think of the subquery as a 'single value expression'.

# Scenario - I
We use a Subquery in the SELECT clause when we need an aggregate value of a table as a new column in the data which we plan to retrieve.

# Example
Write an SQL query to get details of all the students along with the average age for all students.

# SQL Query
SELECT id, name, age, (
        SELECT AVG(age) 
        FROM Student
    ) AS avg_age 
FROM Student;
In the above SQL query, (SELECT AVG(age) FROM Student) is SubQuery. It returns the result 23.65 as avg_age. So, the output contains this result added to each row.

# Result
id	name	age	avg_age
1	Christopher Arwood	22	23.65
2	Cathi Tyson	21	23.65
3	Tracy Bartlebaugh	28	23.65
4	Kevin Lopez	22	23.65
5	Marilyn Sindelar	30	23.65
...	...	...	...
# Scenario - II
We can also use a Subquery in simple expressions in the SELECT clause. That is, it can be used in places where a value, which is used in an expression for computation, has to be dynamically updated (as seen in the first subquery example).

# Example
Let's find the variance of age for each student. The result must have student details and the age variance of the student as an age_variance column.

Formula for age variance

(age of a student - average age of all the students) = (age - avg_age)
# SQL Query
SELECT id, name, age, age - (
        SELECT AVG(age) 
        FROM Student
    ) AS age_variance  
FROM Student;
The expression in the above SQL query is age - (SELECT AVG(age) FROM Student) and (SELECT AVG(age) FROM Student) is the SubQuery.

# Result
id|name|age|age_variance
1|Christopher Arwood|22|-1.65
2|Cathi Tyson|21|-2.65
3|Tracy Bartlebaugh|28|4.35
4|Kevin Lopez|22|-1.65
5|Marilyn Sindelar|30|6.35
..............
# Try it yourself
Write an SQL query to get details of all the students along with the maximum age of the students in database. The result must contain these column fields id, name, age, and max_age
# Result
id	name	age	max_age
1	Christopher Arwood	22	30
2	Cathi Tyson	21	30
3	Tracy Bartlebaugh	28	30
4	Kevin Lopez	22	30
5	Marilyn Sindelar	30	30
...	...	...	...
Write an SQL query to get details of all the students along with the minimum age of the students in database. The result must contain these column fields id, name, age, and min_age
# Result
id	name	age	min_age
1	Christopher Arwood	22	18
2	Cathi Tyson	21	18
3	Tracy Bartlebaugh	28	18
4	Kevin Lopez	22	18
5	Marilyn Sindelar	30	18
Write an SQL query to get details of all the Courses along with avg credits of Courses. The result must contains these column fields id, name, credits, avg_credits
# Result
id	name	credits	avg_credits
1	Numerical Analysis	4	2.65
2	Introduction to Electrical and Electronic Circuits	3	2.65
3	Discrete Structures	4	2.65
4	Data Structures and Algorithms	5	2.65
5	Data Structures and Algorithms Lab	2	2.65
...	....	...	...
Write an SQL query to find the variance of Course credits. The result must have these column fields id, name, avg_credits,and credit_variance
# Result
id	name	avg_credits	credits_variance
1	Numerical Analysis	2.65	1.35
2	Introduction to Electrical and Electronic Circuits	2.65	0.35
3	Discrete Structures	2.65	1.35
4	Data Structures and Algorithms	2.65	2.35
5	Data Structures and Algorithms Lab	2.65	-0.65
...	...	...	...
Write an SQL query to find the variance percentage of student age
variance percentage of student age (variance_percent) = (age - avg_age)/avg_age
avg_age is the variance i.e the difference between age of a student and the average age of all the students.
Your query should return in id, name, age, variance, and variance_percent columns
# Result
id	name	age	variance	variance_percent
1	Christopher Arwood	22	-1.65	-0.0697674418604651
2	Cathi Tyson	21	-2.65	-0.112050739957717
3	Tracy Bartlebaugh	28	4.35	0.183932346723044
4	Kevin Lopez	22	-1.65	-0.0697674418604651
5	Marilyn Sindelar	30	6.35	0.268498942917548
...	...	...	...	...
# Correlated Queries
We can also use an outer query’s value in the subquery. Such subqueries are called as correlated subqueries. The results of that subquery depends on the values in the outer query. Correlated queries are also called as 'synchronized queries'.

In a simple subquery in SELECT clause, the subquery result is the same for all the records in the final output. Whereas, in a correlated subquery, the result of the subquery depends on the values passed from the outer query.

# Example
For each student in the database, find the number of students who are with the same age.(no_of_students_with_same_age).

SELECT id, name, age, (
        SELECT COUNT(age) 
        FROM Student 
        WHERE age=s.age AND id <> s.id
    ) AS no_of_students_with_same_age 
FROM Student AS s;
Here, (SELECT COUNT(age) FROM Student WHERE age=s.age AND id <> s.id) is the subquery and it depends on the values from outer subquery for age and id comparisons. i.e., s.age, s.id are used to filter the records in the inner subquery.

# Result
id	name	age	no_of_students_with_same_age
1	Christopher Arwood	22	13
2	Cathi Tyson	21	5
3	Tracy Bartlebaugh	28	11
4	Kevin Lopez	22	13
5	Marilyn Sindelar	30	6
...	...	...	...
A Correlated subquery need not be executed on the same table which is used in the outer query.
# Example
Get all students' details with their average scores across all of their enrolled courses.

SELECT id, name, age, (
        SELECT AVG(score) 
        FROM Enrollment 
        WHERE student_id = s.id
    ) AS avg_score 
FROM Student s;
Here, (SELECT AVG(score) FROM Enrollment WHERE student_id = s.id) is the subquery and it depends on the outer subquery for student_id i.e s.id, to filter the records in the Enrollment table, to calculate the average score of a particular student.

# Result
id	name	age	avg_score
1	Christopher Arwood	22	51.0
2	Cathi Tyson	21	62.75
3	Tracy Bartlebaugh	28	66.0
4	Kevin Lopez	22	38.0
5	Marilyn Sindelar	30	76.0
...	...	...	...
# Try it yourself
Write an SQL query to get Students' details with the sum of their scores across all of their enrolled courses.
Result should contain these column fields id, name, age, and sum_of_scores.
# Result
id	name	age	sum_of_scores
1	Christopher Arwood	22	102
2	Cathi Tyson	21	251
3	Tracy Bartlebaugh	28	132
4	Kevin Lopez	22	76
5	Marilyn Sindelar	30	76
...	...	...	...
Write an SQL query to get the students' details and their maximum score across all of their enrolled courses.
# Result
id	name	age	max_score
1	Christopher Arwood	22	77
2	Cathi Tyson	21	93
3	Tracy Bartlebaugh	28	79
4	Kevin Lopez	22	46
5	Marilyn Sindelar	30	76
...	...	...	...
# Correlated Subqueries versus Inner Joins
In some cases, you might be able to solve a problem using a Subquery or an Inner Join. For example, you could've used Inner Join to solve the above Correlated Subqueries question.

To get all students' details with their average scores across all of their enrolled courses, we could've written the following SQL query using INNER JOIN.

# Using INNER JOINS
SELECT id, name, age, AVG(es.score) AS avg_score 
FROM (Student as s
        INNER JOIN Enrollment AS es 
        ON s.id = es.student_id)
GROUP BY s.id;
# Using Correlated SubQueries
SELECT id, name, age, (
        SELECT AVG(score) 
        FROM Enrollment 
        WHERE s.id=student_id
    ) AS avg_score 
FROM Student s;
# Result
id	name	age	avg_score
1	Christopher Arwood	22	51.0
2	Cathi Tyson	21	62.75
3	Tracy Bartlebaugh	28	66.0
4	Kevin Lopez	22	38.0
5	Marilyn Sindelar	30	76.0
...	...	...	...
We get the same result using a Correlated Subquery or an Inner Join.

# Key Points
SubQueries could be slower - A correlated subquery could be “executed/run” once for each row returned in the outer query. Whereas, the INNER JOIN will only make one pass through the data. Although there are some exceptions to this behaviour, based on the type of the underlying databased used, it is generally recommended to use Inner Joins in such situations.

Readability wise, depending upon what you’re comfortable with, you may find the INNER JOIN example easier to read than the correlated query.

