Note: You can make use of imdb.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_008. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_008/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specified individually.
#Questions
Get all Budding directors - Find all directors who didn’t direct any film before 2000 and have directed at least one film after 2000. Your query should result in id and fname of the director in ascending order of id.

Sample Output Format:

1 Director1
2 Director2

Query Submission Format:

Q1="Write your query here"


Find the best ranked movie for each director. Incase of more than one movie select the first one when sorted in ascending order of movie name.
Your query should return fname and name of the movie. Your query should return only 100 entries

Sample Output Format:

Director1 Movie1
Director2 Movie2

Query Submission Format:

Q2="Write your query here"

List 100 actors who didn't act in any movie between 1990 and 2000. Your query should return only 100 unique actors when sorted by id in descending order.

Q3="Write your query here"    
