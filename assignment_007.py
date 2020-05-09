Duration: 180 minutes

Note: You can make use of imdb.sqlite3 database given to solve this assignment

# Submission Guidelines
# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_007. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_007/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specified individually.
#Questions
Find the number of movies that are released before 2000 [3 points]

Q1="Write your query here"

Get the average ranking for movies which are released in year 1991

Sample Output Format:

6.912...

Query Submission Format:

Q2="Write your query here"


Get the minimum rank of all the movies which are released in the year 1991 [3 points]

Sample Output Format:

1.2

Query Submission Format:

Q3="Write your query here"  
  

Get fname and lname of all the actors of movie whose id is equal to 27 . [3 points]

Sample Output Format:

tony stark
captain america

Query Submission Format:

Q4="Write your query here"

Count the number of movies in which actor “Jon Dough” has acted. [3 points]
Assume that you can uniquely identify him using the following conditions
fname : “Jon”
lname : “Dough”

Sample Output Format:

10

Query Submission Format:

Q5="Write your query here"


Get names of all movies in “Young Latin Girls” series which are released between 2003 and 2006 [3 points]

Note: Movies whose name starts with “Young Latin Girls” can be treated as movies that belong to the “Young Latin Girls” series

Q6="Write your query here"
Get fname and lname of all directors (unique directors) who directed atleast one movie in Star Trek series [5 points]

Note: You can assume that a movie is in Star Trek movie series if it has “Star Trek” at the beginning of its name

Q7="Write your query here"
Find all movies for which Jackie Chan is both director and actor, Your query results should be in ascending order of name of the movie [5 points]

Note: You can assume that we can identify Jackie Chan uniquely by
fname: Jackie (I) & lname: Chan

Q8="Write your query here"
List fname and lname of directors who directed at least 4 movies which released in 2001. Your query should return results in the following order [5 points]

ascending on fname
and then descending on lname
Q9="Write your query here"   

Write a query to get the number of male and female actors in our database. In the ascending order of gender [5 points]

Sample Output Format:

F 40
M 59
Query Submission Format:

Q10="Write your query here"

Write a query to get movie pairs in which both the movies are released in the same year and have same rating. Your query should result in 100 entries and sorted in ascending order of first movie name. [10 points]
Return only distinct pairs i.e pairs (Movie1, Movie2) and (Movie2, Movie1) should be considered as same.

Sample Output Format:

MovieName1 MovieName2 8 2000 
MovieName3 MovieName4 8 2001 

Query Submission Format:

Q11="Write your query here"    
Rank of an actor for a given year is the average of ranks of all the movies he/she is casted in and released in that year. Your query should result fname, year and the rank of the actors. Your query should result in only 100 entries when ordered as following [10 points]

ascending order on actor fname and then
descending order on year
Sample Output Format:

Actor1 2001 9 
Actor1 2000 8

Query Submission Format:

Q12="Write your query here"
Find the top Actor - Directors pair.
The score for an Actor - Director pair is the average of ranks of movies which the director has directed and which the actor has acted. Consider only Actor - Director pair if they have worked together for at least 5 movies. [10 points]

Your query should return fname of the actor, fname of the director and the score.

Your query should return first 100 such pairs when ordered in

descending order of score and then
ascending order of director fname and then
descending order of actor fname
Sample Output Format:

Actor1 Director1 10.0
Actor2 Director2 8.0

Query Submission Format:

Q13="Write your query here"

