iBHubs

Home
AssignmentID - DB014
Submission Guidelines
Coding Guidelines
Problem Statement
Aggregations
avg()
min()
max()
sum()
count()
Task1:
Task2:
Task3:
Task4:
Task5:
Learning Material
# Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_014. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_014/
#Coding Guidelines
Write your code in student.py
# Problem Statement
A Student has name, age, score and student_id attributes, Where student_id value is unique for each student object.

Student class for the above mentioned details:

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score

    ...

Make use of the above code snippet.

In the previous assignment you have implemented get, save, delete, filter methods.

In this assignment you will be implementing the aggregations methods.

# Aggregations
In database management, an aggregation function is a function where the values of multiple rows are grouped together as input on certain criteria to form a single value of more significant meaning.

Reference to SQL Aggregations

In this, you are going to implement the below aggregation methods

avg
count
max
min
sum
Your aggregation methods should support the following conditional operations

Equals
Less Than
Less Than Or Equal To
Greater Than
Greater Than Or Equal To
Not Equal To
In
Contains
# Data in Table
student_id	name	age	score
1	Maude Vanhorne	23	89
2	Sarah Kirwan	34	44
3	Fletcher Lomago	40	10
4	Jesse Couch	34	62
5	Israel Gilliland	38	77
6	Michael Aguas	34	87
7	Stephen Boone	25	39
8	Brandon Ashton	24	16
9	Cynthia Knuth	32	17
10	Hazel Wood	35	8
# avg()
avg() function is used to calculate the average of values for the particular field. It should take two parameters one parameter is the field for which you need to calculate average and another is **kwargs which takes conditions, it is an optional parameter.

# Example1
>>> avg_age = Student.avg('age')
>>> avg_age
31.9
# Explanation
The above method returns the average of all ages present in the database.

# Example2
>>> avg_age = Student.avg('age', age__gt=18)
>>> avg_age
31.9
# Explanation
The above method returns the average of all ages present in the database where the age is greater than 18.

# Example3
>>> avg_age = Student.avg('age', age__gt=18, age__lt=21)
>>> avg_age
35.28
# Explanation
The above method returns the average of all ages present in the database where the age is greater than 18 and less than 21.

# min()
min() function is used to calculate the minimum value of the particular field. It should take two parameters one parameter is the field for which you need to calculate minimum value and another is **kwargs which takes conditions, it is an optional parameter.

# Example1
>>> min_age = Student.min('age')
>>> min_age
23
# Explanation
The above method returns the minimum age from all student ages present in the database.

# Example2
>>> min_age = Student.min('age', age__gt=18)
>>> min_age
32
# Explanation
The above method returns the minimum age from all students ages present in the database where the age is greater than 18.

# Example3
>>> min_age = Student.min('age', age__gt=18, age__lt=21)
>>> min_age
19
# Explanation
The above method returns the minimum age from all students ages present in the database where the age is greater than 18 and less than 21.

# max()
max() function is used to calculate the maximum value of the particular field. It should take two parameters one parameter is the field for which you need to calculate maximum value and another is **kwargs which takes conditions.

It is similar to min().

# sum()
sum() method is used to calculate the sum of values. It should take two parameters one parameter is the field for which you need to calculate sum and another is **kwargs which takes conditions, it is an optional parameter.

# Example1:
>>> sum_of_age = Student.sum('age')
>>> sum_of_age
319
# Explanation:
The above method returns the sum of all ages in present in the database.

# Example2:
>>> sum_of_age = Student.sum('age', score__gt=30)
>>> sum_of_age
188
# Explanation:
The above method returns the sum of all ages present in the database where the score is greater than 30.

# Example3:
>>> sum_of_age = Student.sum('age', score__gt=30, age__lt=30)
>>> sum_of_age
48
# Explanation:
The above method returns the sum of all ages in the present in the database where the score is greater than 30 and age is less than 30.

# count()
count() method is an aggregate function that returns the number of rows returned by a query. It should take two parameters optional parameters, one parameter is the field for which you need to calculate sum and another is **kwargs which takes conditions.

# Example1:
>>> count = Student.count()
>>> count
10
# Explanation:
The above method returns number of rows present in the database.

# Example2:
>>> count = Student.count('age')
>>> count
10
# Explanation:
The above method returns count of age fields found in a database.

# Example3:
>>> count = Student.count('age', score__gt=30, age__lt=30)
>>> count
2
# Explanation:
The above method returns the count of age fields found in a database where the score is greater than 30 and age is less than 30.

Note: It should raise an exception for an invalid field.
# Task1:
Implement avg() method which will works for all conditional operations as mentioned in the above.
@classmethod
def avg(cls, field, **kwargs):
    pass
# Task2:
Implement min() method which will works for all conditional operations as mentioned in the above.
@classmethod
def min(cls, field, **kwargs):
    pass
# Task3:
Implement max() method which will works for all conditional operations as mentioned in the above.
@classmethod
def max(cls, field, **kwargs):
    pass
# Task4:
Implement sum() method which will works for all conditional operations as mentioned in the above.
@classmethod
def sum(cls, field, **kwargs):
    pass
# Task5:
Implement count() method which will works for all conditional operations as mentioned in the above.
@classmethod
def count(cls, field, **kwargs):
    pass
# Learning Material
Sample python snippets to execute SQL queries.
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

Reference to access sqlite3 database using python.
Note: Test cases for your submissions are executed on students.sqlite3 database with Student table created using the below SQL query.

CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(250),
    age INT,
    score INT
);
Learn defining custom exceptions in Python in this reference

