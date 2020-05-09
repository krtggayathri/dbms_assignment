Exam Duration: 180 minutes
Max Score: 43 Points

Note: You can make use of soccer.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/database_submissions/dbms_assignment_009. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/database_submissions/dbms_assignment_009/

# Know your data


Tables:

Team
Match
Player
MatchTeamDetails:
MatchCaptain
GoalDetails
Coding Guidelines:

Write your queries in query.py
Query for each question is to be assigned to a variable in the above metioned python file.
# Query Submission Guideline
Assign your query string to a variable with name have the following format

Q{question Number}="Write your query here"

Below are variable names for question 1 and 2 queries

Q1="Write your query here"
Q2="Write your query here"

#Questions
# Task 1
Get the average age of all the players in the database - [2 Points]

# Sample Output Format
3.245989213123125123

# Task 2
Get match_no and play_date of all the matches which have more than 50000 audience - [2 Points]
Your query should return match_no, play_date in ascending order of match_no.

# Sample Output Format
1	2016-06-11
2	2016-02-12
3	2018-02-01

# Task 3
Get the team_id and the number of matches the team has won for each team in the database (Only consider teams which have played atleast one match) - [2 Points]
Your query should return in the descending order of the number of matches won and then in the ascending ordering of team_id

# Sample Output Format
10012	4
10013	3
10014	0

# Task 4
Get the match_no, play_date for all matches whose stop1_sec is greater than average stop1_sec across all matches - [3 Points]
Your query should return match_no and play_date in descending order of match_no

# Sample Output Format
  3	2016-06-11
  2	2016-04-11
  1	2016-02-11

# Task 5
Get the team names and their captain names for all the matches in the database - [3 Points]
Your query should return match_no, team name and the captain name in ascending order of match_no and team name

# Sample Output Format
1	UK	Rob
1	USA	Mike
3	UK	John

# Task 6
Get the name of the player_of_the_match and his/her jersey_no for all the matches in the database - [3 Points]
Your query should result in match_no, player name and his/her jersey_no in ascending order of match_no

# Sample Output Format
 1	Mike	6
 2	Rob	8
 3	Pike	1

# Task 7
Get the team name and the average age of players in that team for all the teams whose average age is greater than 26 - [3 Points]
Your query should result in team name and average_age in ascending order of name

# Sample Output Format
UK	38.3
USA	27.5

# Task 8
Get the total number of goals scored by all players whose age is less than or equal to 27 - [3 Points]
Your query should return player name, jersey_no, age and the number of goals scored in the descending order of the number of goals and then ascending order of player name. (Consider only the players who scored atleast one goal)

# Sample Output Format
Rob	4	23	8
Pike	3	21	6
John	1	22	3

# Task 9
Get the percentage of goals each team has scored. - [5 Points]
percentage of goals scored by a team = (total number of goals scored by the team across all matches * 100) / total number of goals scored by all the teams acrosss all matches
Your query should return the team_id and the percentage of goals. (Consider only the teams which scored atleast one goal)

# Sample Output Format
   1	9.41234..
   2	30.58766..
   3	60.0

# Task 10
Get the average of total number of goals scored by a team across all the matches - [5 Points]

# Sample Output Format
1.8

# Task 11
Get all the players who didn’t score in any of the matches. - [5 Points]
Your query should return player_id, name and date_of_birth in the ascending order of player_id.

# Sample Output Format
1	Rob	1989-03-10	 
2	Mike	1989-03-10	 
3	Bob	1989-03-10	 

# Task 12
Get the audience count and the difference between the audience count and the teams average audience count for all matches in the database. - [7 Points]
Your query should return team_name, match_no, audience and the difference beteween the audience and the average audience across all matches played by that team in the ascending order of match_no

# Sample Output Format
USA	1	300000   12340
UK	2	123123  12340
Germany	3	123523  12340
_________________________________________________________________________________________________________





Q1='''SELECT AVG(age) FROM player'''
Q2='''SELECT match_no,play_date FROM match WHERE audience>50000 ORDER By match_no ASC;'''
Q3='''SELECT team_id, count(win_lose) as no_of_matches FROM MatchTeamDetails WHERE win_lose='W' GROUP BY team_id order by no_of_matches desc, 
team_id asc;'''

Q4='''SELECT match_no,play_date FROM match WHERE stop1_sec>
(SELECT AVG(stop1_sec) FROM match) order BY match_no DESC;'''

Q5='''SELECT mtd.match_no,t.name,p.name FROM ((Team as t INNER JOIN Matchcaptain as mtd on 
t.team_id=mtd.team_id)INNER JOIN Player as p on p.player_id=mtd.captain) ORDER BY mtd.match_no asc,t.name asc;'''

Q6='''SELECT match_no,name,jersey_no FROM match INNER JOIN player on player_id=player_of_match order BY match_no;'''

Q7='''SELECT name,(SELECT avg(age) FROM player p  WHERE t.team_id=p.team_id) As avg_age  FROM team as t 
WHERE avg_age>26 order by name ;'''
Q8='''SELECT mtd.name,mtd.jersey_no,mtd.age ,count(goal_id) as no_of_goals FROM goaldetails as t INNER JOIN player mtd on
t.player_id=mtd.player_id where age<=27  
group by mtd.player_id order by no_of_goals DESC,mtd.name ASC;'''

Q10='''SELECT avg(count_goals) FROM (SELECT count(goal_id) as count_goals FROM goaldetails
GROUP By team_id);'''
Q11='''SELECT player_id,name,date_of_birth FROM player as p WHERE NOT EXISTS 
(SELECT goal_id from goaldetails as g WHERE g.player_id=p.player_id)'''

Q9='''SELECT team_id,count(goal_id)*100.0/(select count(goal_id) from goaldetails) from goaldetails group By team_id;'''





Q12='''SELECT t.name,m.match_no,m.audience,
m.audience-(SELECT avg(audience)
FROM matchcaptain as mtc INNER JOIN match as m on mtc.match_no=m.match_no where t.team_id=mtc.team_id)
FROM match m INNER JOIN matchcaptain as mtc on mtc.match_no=m.match_no
INNER JOIN team as t on t.team_id=mtc.team_id dc
order by m.match_no asc;'''


