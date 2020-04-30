QUESTION:
__________________________

assignment_003.md

# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_003. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_003/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specific individually.
Schema for the tables that are to be used for following queries

 Actor (  
	 id integer PRIMARY KEY,
	 fname varchar(250),  
	 lname varchar(250), 
	 gender varchar(10) 
 );

 Movie(  
	 id integer PRIMARY KEY, 
	 name varchar(250), 
	 year integer, 
	 rank integer
 );
	
 Director(  
	 id integer PRIMARY KEY, 
	 fname varchar(250), 
	 lname varchar(250)
 );
 



Get the total number of movies that are released in year 1991
Q1="Write your query here"
...


Get the least rank for a movies
...
Q2="Write your query here"
...


Get the maximum rank for movies that are released in year 2000
...
Q3="Write your query here"
...


Get the average ranking for movies that are released in year 2000
...
Q4="Write your query here"
...

Find the total number of unique years in the imdb database given to you.
...
Q5="Write your query here"
...


Find the time period that this database covers. (start year, end year)
...
Q6="Write your query here"
...


__________________________________________________________________________________________________________________

Q1='SELECT * FROM Movie  ORDER BY rank DESC LIMIT 10;'

Q2='SELECT * FROM Movie  ORDER BY rank DESC LIMIT 10 OFFSET 10;'

Q3='SELECT name FROM Movie WHERE year>2004'

Q4='SELECT name FROM Movie WHERE rank<1.1'

Q5='SELECT * FROM Movie WHERE year IN (2004,2005,2006)'

Q6='SELECT name,year FROM Movie WHERE name LIKE "Harry%";'

Q7='SELECT * FROM Actor WHERE (fname="Christin") AND (lname!="Watson")'

Q8='SELECT * FROM Actor WHERE (fname="Woody") AND (lname="Watson")'

Q9='SELECT name FROM Movie WHERE year=1990 AND rank=5'

Q10='SELECT * FROM Actor WHERE (fname="Christin") AND (lname="Watson")'

Q11='SELECT name FROM Movie WHERE year BETWEEN 2003 AND 2005'

Q12='SELECT DISTINCT year FROM Movie ORDER BY year ASC'

Q13='''SELECT * FROM Actor WHERE (fname="Christin") OR (lname="Watson") AND 
        (gender="M") ORDER BY fname ASC LIMIT 10'''
____________________________________________________________________________________



