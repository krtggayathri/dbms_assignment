Many to Many relationships

In a many-to-many relationship, a single record in the first table can be related to 0, one or many records in the second table and vice versa.

Unlike One To Many relation, adding a foreign key in the first table or in the second table or in both the tables wouldn't be sufficient to represent a Many to Many Relationship.

Adding a foreign key in a table means you have fixed that an entry in that table is related to at most one entry in the other table. So, even if you add foreign keys in both the tables to each other, you can only relate a record in one table to at most one entry in the other table.

To implement a many-to-many relation, we must use a mapping or intermediate or junction table. This intermediate table contains foreign keys to both the tables which have the many-to-many relationship.

# Scenario
Let's look at an example. Employees can work on various projects and a project can have many employees working on it.

Employee table has the following fields

employee_id - int - primary key
name - string
salary - float
Project table has the following fields

project_id - int - primary key
title - string
EmployeeProjects is an intermediate table which contains

employee_id - foreign key to Employee table
project_id - foreign key to Projecttable
# Creating Many-to-Many relationship
Create Employee table
CREATE TABLE Employee (employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(100), 
                       salary FLOAT);
Create Project table
CREATE TABLE Project(project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title VARCHAR(100));
Create an intermediate table called EmployeeProjects
CREATE TABLE EmployeeProjects(project_id INTEGER NOT NULL, 
                            employee_id INTEGER NOT NULL, 
                            project_details_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            FOREIGN KEY (employee_id)REFERENCES Employee (employee_id), 
                            FOREIGN KEY (project_id)REFERENCES Project (project_id));

# Inserting data
Insert data into Employee table
INSERT INTO Employee(name, salary)values('John',200000);  
INSERT INTO Employee(name, salary)values('Ram',300000);
Insert data into Project table
INSERT INTO Project(title)values('imdb');  
INSERT INTO Project(title)values('dashboards');
An employee working on a project is represented only by the corresponding entry in the EmployeeProjects table.
INSERT INTO EmployeeProjects(project_id, employee_id)values(1,1);  
INSERT INTO EmployeeProjects(project_id, employee_id)values(1,2);  
INSERT INTO EmployeeProjects(project_id, employee_id)values(2,1);  
# Explanation
EmployeeProjects table contains the following data

project_id	employee_id
1	1
1	2
2	1
Employee with employee_id=1 is working on projects with project_id= 1 & 2

Employee with employee_id=2 is working on a project with project_id= 1

# Example
Write a query to fetch all employees' ids working on project 1.
sqlite> SELECT employee_id FROM EmployeeProjects WHERE project_id=1;
# Result
employee_id
1
2
Write a query to fetch project_ids of employee 1
sqlite> SELECT project_id FROM EmployeeProjects WHERE employee_id=1;
# Result
project_id
1
2
Note
Intermediate table can also be used to store data other than the Foreign Key fields. Any data that is an attribute/property of the relationship between the two tables can be stored in the intermediate table.

For example: Group and Person are two tables having a many-to-many relationship. And let Membership be the intermediate table. For a person, the date of joining a group can be stored in the Membership table. Notice that, Membership table is the only appropriate table to store such information because it's an attribute/property of the 'Person joining the Group' and not that of any the Person or the Group alone.

# Try it yourself
Create a Student table with the following fields

student_id
name
age
marks
Create a Course table with the following fields

course_id
title
Create an Enrollment table with the following fields

student_id
course_id
Insert the following data in Student table.

student_id	name	age	marks
1	John	20	90.0
2	Ron	22	98.0
3	Ram	19	91.0
Insert the following data in Course table.
course_id	title
1	Data Structures
2	Artificial Intelligence
3	Art of Cooking
4	Mythology
5	English Literature
Insert the following data in Enrollement table.
enrollment_id	course_id	student_id
1	1	1
2	2	1
3	3	1
4	4	1
5	5	1
6	1	2
7	2	2
8	3	2
9	4	2
10	1	3
11	2	3
Write an SQL query to get student_ids who enrolled in the Course with course_id=1
# Expected Output
student_id
1
2
3
Write an SQL query to get all the course_ids in which student with student_id=1 has enrolled
# Expected Output
course_id
1
2
3
4
5
