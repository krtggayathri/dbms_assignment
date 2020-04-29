question:
create imdb.sqlite3 from 3 tables


assignment_002.md

# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_002. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_002/
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


Get top 10 movies when sorted in descending order of rank
...
Q1="Write your query here"
...


Get top 10 movies in descending order of rank skipping first 10.
...
Q2="Write your query here"
...

Get all the movie names which are released after 2004
...
Q3="Write your query here"
...


Get names of all movies which have rank less than 1.1
...
Q4="Write your query here"
...

Get all the movies which released in 2004, 2005, 2006
...
Q5="Write your query here"
...

Get name and year of releases for the movies which start with Harry in its name
...
Q6="Write your query here"
...


Get all the actors whose first name is Christin and last name is not Watson
...
Q7="Write your query here"
...

Get all the actors whose first name is Woody and last name is Watson
...
Q8="Write your query here"
...


Get name of movies which are released in the year 1990 and have rank equal to 5
...
Q9="Write your query here"
...

Get all the actors whose first_name is Christin or last_name is Watson
...
Q10="Write your query here"
...

Get all the movie names which are released between 2003 and 2005 (inclusion of 2003 and 2005)
...
Q11="Write your query here"
...

Get distinct years in which movies are released in ascending order
...
Q12="Write your query here"
...

Get top 10 actors whose
first_name is Christin or last name is Watson
And gender is Male(M)
in alphabetically sorted by first name.
...
Q13="Write your query here"
...


___________________________________________________________________________________________________________________


answer:
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
        
        





