Q1='SELECT pid AS actor_id,COUNT(mid) AS no_of_movies FROM Cast GROUP BY pid'
Q2='SELECT year,COUNT(ID) FROM Movie GROUP BY year ORDER BY year ASC'
Q3='''SELECT year,AVG(rank) AS avg_rank FROM Movie GROUP BY year Having count(year)>10 
         ORDER BY year DESC '''
Q4='SELECT year,MAX(rank) AS max_rank FROM Movie GROUP BY year ORDER BY year ASC'
Q5='SELECT rank,COUNT(name) FROM Movie WHERE name LIKE "a%" GROUP BY rank'

__________________________________________________________________________________________

iBHubs

Home
AssignmentID - DB005
Submission Guidelines
Coding Guidelines
Tasks
Task 1
Task 2
Task 3
Task 4
Task 5
# Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_005. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_005/
#Coding Guidelines
Write your queries in query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specified individually.
Schema for the tables that are to be used for following tasks

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

Cast(
        pid integer,
        mid integer,
        role varchar(200)
    );

MovieDirector(
        did integer,
        mid integer
    );

Cast stores the cast data i.e the actors who acted in each movie.

pid - actor id
mid - movie id
role - role of the actor with id equal to pid in movie with id equal mid
Similar to Cast, MovieDirector stores movie directors data i.e the directors for each movie

# Tasks
# Task 1
Calculate the number of movies(no_of_movies), each actor(actor_id) has acted.

Q1="Write your query here"
...

# Output Format
actor_id    no_of_movies
    1           10
    2           7
....
# Task 2
Calculate the number of movies released in each year, results should be in the ascending order of year.

...
Q2="Write your query here"
...
# Output Format
year    count
2001     10
2002     7
....
# Task 3
Calculate the average rank of movies(avg_rank) for each year, return year and avg_rank for years in which atleast 10 movies are released. Results should be in the descending order of year.

...
Q3="Write your query here"
...
# Output Format
year    avg_rank
2010        9
...
# Task 4
Calculate the maximum rank of movies(max_rank) for each year, return year and max_rank. Results should be in the ascending order of year.

...
Q4="Write your query here"
...

# Output Format
year    max_rank
2010        9
...
# Task 5
Calculate the number of movies whose name starts with "a" and have the same rank, return rank, and the number of movies for that rank.

...
Q5="Write your query here"
...
# Output Format
rank    no_of_movies
  9        111
...
