Q1='''SELECT fname,lname FROM Actor INNER  JOIN Cast on id=pid WHERE mid=12148'''
Q2='''SELECT COUNT(mid) FROM Actor INNER JOIN Cast on id==pid WHERE 
        fname="Harrison (I)" and lname="Ford" '''
 
Q3='''SELECT DISTINCT pid FROM Movie INNER JOIN Cast on id=mid WHERE name LIKE "Young Latin Girls%";'''                       
       

Q4='''SELECT COUNT(DISTINCT pid) FROM Movie INNER JOIN Cast on id==mid 
        WHERE year BETWEEN 1990 AND 2000;'''
        
 ____________________________________________________________________________________________
iBHubs

Home
AssignmentID - DB006
Submission Guidelines
Coding Guidelines
# Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_006. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_006

#Coding Guidelines
Write your queries query.py

Query for each question is to be assigned to a variable in the above python file. Variables for each question are specific individually.

Get fname and lname all the actors casted in movie_id = 12148

Q1="Write your query here"
...

Count the number of movies in which actor “Harrison (I) Ford” acted
first name: “Harrison (I)”
last name: “Ford”
...
Q2="Write your query here"
...


Get all the distinct actors ids who acted in all movie whose title starts with Young Latin Girls.
...
Q3="Write your query here"
...


How many distinct actors have acted in any movie between 1990 and 2000 (both inclusive).
...
Q4="Write your query here"
...


