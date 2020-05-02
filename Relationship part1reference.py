iBHubs

Home
SQL
Conclusion
Relationship
Different Types of Relationships
One To One Relationship
One To Many Relationship
Many To Many Relationship
# Introduction - Need for multiple tables

So far, we've learnt how to add, update, delete and retrieve data from a single table. In a typical web application, data is stored in multiple tables.

Why do we need to store data in multiple tables?

Having all the application data in a single table is highly inefficient and is not scalable. Let's look at some of the problems:

Data Duplication
Insertion Anomaly
Updation Anomaly
Deletion Anomaly
Poor naming convention
Let's understand these problems using the below table which stores the students' branch information in a university.

roll_no	name	branch	hod	office_tel
401	Akon	CSE	Yon	53337
938	Ram	CSE	Yon	53337
168	John	CSE	Yon	53337
113	Akash	CSE	Yon	53337
190	Giri	CSE	Yon	53337
919	Lakshman	CSE	Yon	53337
# Data Duplication
In the above table if we have to insert data of 100 students of same branch, then the branch information has to be repeated (Duplicate Data) for all those 100 students in the table. This increases the storage space required and decreases the performance of the database.

One of the major factors that effects the performance of an SQL query is the number of rows it has to deal with.

Let's say we have 3 branches with each having 1000 students registered. Inorder to process SQL query to retrieve the Branch details, the DB has to handle all the data (i.e 3x 1000) due to data duplication. This would be much slower than handling 3 entries, in case we had stored branch data in a separate table.

# Insertion Anomaly
If you observe the DB schema (which has just 1 table), we cannot add a branch without adding any students to our database. This is a serious constraint for a developer to design applications based on this database.

# Updation Anomaly
Let's say a new person has been appointed as HOD of the CSE department.

To update this information in our database, we need to update all the CSE department student records in the database which is highly inefficient. In the above example, if the department has 1000 students, then we need to update 1000 rows to update the HOD details!

Also, failure in updation to any of these rows could lead to data inconsistency. i.e, updated rows will have a different HOD compared to the not-updated(old) rows. If you try to retrieve HOD of CSE department from such a table, you will get two entries! - old HOD and new HOD. But, logically, a department cannot have more than one HOD.

# Deletion Anomaly
In the above table, two different categories of information i.e., Student and Branch information are stored together. If we have to delete all the student records of a particular branch for some reason, we will also lose the branch & hod information as well. This again poses unreasonable constraints on application design.

# Poor naming conventions
The table name must describe the data it holds, and each column name must describe the information it represents.

If we have to name the above table, we cannot choose

Branch - as the table contains student information as well.
Student - as the table contains branch information as well.
You might think StudentBranch could be a good name. But, remember, to build a meaningful application, we need more and more types of data to be stored.

A simple extension for the above example is to add Course information as well. How would we name the table then? It keeps getting complicated as we add more columns.

# Not easy to extend
So, simple extensions like adding Course data and maintaining students registration in those courses will introduce a lot more redundancy and makes the table much bulkier.

# Conclusion
From all the above problems, it is evident that we can not store all the application data in a single table. So, each row has to be split into smaller parts and stored in separate tables.

Then, how would we keep track of which row in table A is related to which row in table B? In databases, we use relationships to keep track of related rows in different tables.

# Relationship
A relationship between two tables represents how 'a row in the first table' is related to 'a row in the second table.' Relationships make it possible to split and store data in multiple tables to avoid duplication and insertion, updation, deletion anomalies.

# Different Types of Relationships
There are four types of relationships

One To One Relationship
One To Many Relationship
Many To One Relationship
Many To Many Relationship
# One To One Relationship
In a one-to-one relationship, a row in first table is related to at most one row of the second table.

# Example1:
Let's say, we are storing Users and their Aadhar details in our database. You might already know that, a user can have only one Aadhar details and any Aadhar details (i.e aadhar number etc.,) can be associated to only one user. So we say Users and AadharDetails have a OneToOne relationship.

# One To Many Relationship
In a one-to-many relationship, a single record in the first table can be related to one or more records in the second table. But, a single record in the second table can be related to at most one record in the first table.

First table is referred as the Parent Table and the second table as Child Table.

# Example
Let's say, we are storing Customer and their Order details in our database.

A Customer can create many Orders but an Order is always associated to a single Customer. Two customers cannot create the same order (i.e order with same order-id or order number).

Note
Many To One Relationship is just looking at the One To Many Relationship from other table's perspective.

# Many To Many Relationship
In a many-to-many relationship, a single record in the first table can be related to 0, one or many records in the second table and vice versa.

# Example
Let's say, we are storing Author and their Book details in our database.

An Author can write write many Books. A Book can be co-authored by multiple Authors.

