Q1='''select a.id,a.fname,a.lname,a.gender FROM Actor as a 
INNER JOIN cast as c on c.pid=a.id 
INNER JOIN Movie as m on m.id=c.mid 
WHERE m.name LIKE "Annie%"
'''
Q2='''select m.id,m.name,m.rank,m.year FROM Movie as m 
INNER JOIN MovieDirector as md on md.mid=m.id 
INNER JOIN Director as d on d.id=md.did
WHERE (fname="Biff" and lname="Malibu") and year IN (1999,1994,2003)
ORDER By rank desc,year ASC;
'''
Q3='''select year,count(id) as no_of_movies FROM movie GROUP By year 
HAVING AVG(rank)>(select avg(rank) from movie) order by year asc;
'''
Q4='''select id,name,year,rank FROM Movie where year=2001 and rank<(select avg(rank) 
FROM Movie where year=2001) order by rank desc limit 10;
'''
Q5='''SELECT m.id,
(SELECT count(a.gender) from Actor as a 
INNER JOIN cast as c on c.pid=a.id where c.mid=m.id and gender='M') as no_of_males,
(SELECT count(a.gender) from Actor as a 
INNER JOIN cast as c on c.pid=a.id where  c.mid=m.id and gender='F' ) as no_of_females
from Movie as m order by m.id ASC limit 10;
'''

Q6='''select c.pid from cast as c INNER JOIN Actor as a on  a.id=c.pid 
group by c.pid,c.mid having count(distinct role)>1 order by c.pid ASC;
'''


Q7='''select fname,count(id) FROM director group by fname having count(fname)>1;
'''

Q8='''select d.id,d.fname,d.lname FROM director as d
WHERE EXISTS
(select c.pid From MovieDirector as md
INNER JOIN Cast as c on c.mid=md.mid where d.id=md.did group by md.mid having count(distinct pid)>=100) 
AND NOT EXISTS
(select c.pid From MovieDirector as md
INNER JOIN Cast as c on c.mid=md.mid where d.id=md.did group by md.mid having count(distinct pid)<100) 
'''

Q5='''select no_of_males.pid,no_of_males.md,no_of_females.pid,no_of_females.fd
FROM(
select pid,count(gender) as md from Actor 
INNER JOIN Cast on pid=id where
 gender='M') AS no_of_males JOIN
 (
select pid,count(gender) as fd from Actor 
INNER JOIN Cast on pid=id where
 gender='F') AS no_of_females
 


''' 
_____________________________________________________________________________________________________________________

Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_011. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_011/
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
Get list of all the actors who casted in all the movies having name starting with 'Annie'

Q1="Write your query here"
...

# Output Format
id|fname|lname|gender
14252|Nuno|Antunes|M
33403|Curtis|Bechdholt|M
54193|Chris (I)|Bradford|M
58118|Lenno|Britos|M
58215|Michael (II)|Britton|M
....
# Task 2
Get the top ranked movies directed by Biff Mailbu (i.e fname = "Biff" and lname = "Malibu") and released in the years (1999, 1994, 2003) in the descending order of rank and ascending order of year.

...
Q2="Write your query here"
...
# Output Format
id|name|rank|year
228066|Nasty Nymphos (1994)|9|1994
# Task 3
For each year find the no_of_movies released in that year. Select year for which average rank of all the movies in that year is greater than the average rank for all movies in the database. Your result should be in the ascending order of year.

...
Q3="Write your query here"
...
# Output Format
year|no_of_movies
1981|1430
1982|353
1983|372
1984|403
1985|439
..........
# Task 4
Get the 10 movies released in the year 2001 whose rank is less than the average rank of all the movies released in that year, when ordered in the descending order of rank.

...
Q4="Write your query here"
...

# Output Format
id|name|year|rank
346246|Undercover X (2001)|2001|10
302296|Simulacra (2001)|2001|9.7
64230|Cinquantenaire du deuxime sexe, 1949-1999 (2001)|2001|9.4
142881|Henry and Marvin (2001)|2001|9.4
43908|Book of Blues (2001)|2001|9.1
2290|32nd NAACP Image Awards (2001)|2001|9
7032|Adventures of Mammary Man and Jugg Woman, The (2001)|2001|9
10943|Aliento (2001)|2001|9
19774|Arca, El (2001)|2001|9
21955|Asian Street Hookers 22 (2001)|2001|9
# Task 5
Get 100 movies with male and female actors cast count when sorted in ascending order of id.

...
Q5="Write your query here"
...
# Output Format
movie_id|no_of_female_actors|no_of_male_actors
322|6|25
351|1|3
898|1|0
961|0|2
1356|3|6
...
# Task 6
Get 100 distinct actor ids who are casted in the same movie for more than one role (different role name) when sorted in ascending order of actor id.

...
Q6="Write your query here"
...
# Output Format
pid
100123
123123
...
# Task 7
Find the number of directors with same first name (fname) in the database (consider fname if more than one director have the it).

...
Q7="Write your query here"
...
# Output Format
fname|count
Ethan|10
...
# Task 8
Get all the directors who directed only movies having unique cast more than 100

...
Q8="Write your query here"
...
# Output Format
id|fname|lname
500|Marc F.|Adler
843|Zoya|Akhtar
1427|Michael|Almereyda
2639|Jeff|Arch
3641|Omar Abdel|Aziz
............


