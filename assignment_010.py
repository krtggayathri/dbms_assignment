Note: You can make use of soccer.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/database_submissions/dbms_assignment_010. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/database_submissions/dbms_assignment_010/

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
Find all the players in the database who acted as captain for at-least one match and didn't make at least one goal.

# Sample Output Format
player_id|team_id|jersey_no|name|date_of_birth|age
160140|1207|1|Hugo Lloris|1986-12-26|29
160349|1216|6|Vlad Chiriches|1989-11-14|26
160013|1201|5|Lorik Cana|1983-07-27|32
160467|1221|2|Stephan Lichtsteiner|1984-01-16|32
160401|1218|3|Martin Skrtel|1984-12-15|31
..............
# Task 2
Find the number of games played by each team

# Sample Output Format
team_id|no_of_games
1201|3
1202|3
1203|5
1204|4
1205|3
........
# Task 3
Find the average goal score of each team. The average goal score for a team is the total number of goals divided by the total number of members in the team.

# Sample Output Format
team_id|avg_goal_score
1201|0.0434782608695652
1202|0.0434782608695652
1203|0.391304347826087
1204|0.217391304347826
1205|0.0869565217391304
.......
# Task 4
For each captain find the number of matches he/she has been captain to that match. The result should have captain and no_of_times_captain columns as shown below.

# Sample Output Format
captain|no_of_times_captain
160004|2
160013|1
160028|3
160062|5
160076|4
...........
# Task 5
Find the number of players(no_players) who are captain and also awarded the player of the match for the same match.

# Sample Output Format
no_players
6
# Task 6
Find the distinct player ids who are captain for atleast one match and didn't get the player of the match title for even a single match.

# Sample Output Format
captain
160004
160004
........
# Task 7
Find the number of matches played in each month. Your query should return Month and no_of_matches in the descending order of no_of_matches

# Sample Output Format
month|no_of_matches
06|44
...
# Task 8
Find the jersey number and the number of captains use it. Your query should return jersey_no and no_captains in the descending order of no_captains and jersey_no.

# Sample Output Format
jersey_no|no_captains
1|17
....
# Task 9
Find the average of the audience for each player. In the descending order of avg_audience and player_id.

# Sample Output Format
player_id|avg_audience
160001|49075.66
160002|145675.123
160003|97234.66
160004|72345.852
160005|91203.123
...
# Task 10
Calculate the average age of players for each team.

# Sample Output Format
team_id|AVG(age)
1201|27.0869565217391
1202|27.2173913043478
1203|25.9130434782609
1204|26.304347826087
1205|28.7391304347826
......... 

# Task 11
Calculate the average age of all the captains in the database.

# Sample Output Format
avg_age_of_captains
30.6078431372549	 

# Task 12
Find the month and the number of players born in that month in the descending order of no_of_players and month.

# Sample Output Format
month|no_of_players
01|59
....
# Task 13
Find the captain id and the number of matches he/she has won(no_of_wins). Your Query should return captain and no_of_wins in the descending order of no_of_wins.

# Sample Output Format
captain|no_of_wins
160140|5
160163|4
160322|4
160539|4
160062|3
.........

