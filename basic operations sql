question:1
Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_001. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_001/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specific individually.
#Question
Create a User table with following columns
user_id - an integer to unique identify
first_name - string value of max length 200 to store the first name and can not be empty.
last_name -string value of max length 200 to store the last name and can not be empty.
address - string value of max length 300 to store the address and can not be empty.
phone_number - phone number must be integer and cannot be empty
Note: Use exact field names

# query.py
Q1="Write your query here"
...
Create a table to store Post data. We need to store the following data for each of the post

user_id - an integer - id of the user who created this post

post_id - an integer to uniquely identify a Post. Whenever a post is created post_id should be automatically set to a unique integer.

post_content - string value of max length 500 to store the post content.

Note :

Use exact field names
On deleting a particular user corresponding post posted by user should be deleted
...
Q2="Write your query here"
...
Create a user tony stark with the following data
user_id - 1
first_name: tony
last_name : stark
address : new york
phone_number : 1234567890
...
Q3="Write your query here"
...
Create another user John wick with the following data
user_id : 2
first_name: john
last_name : wick
address: la
phone_number : 987654321
...
Q4="Write your query here"
...
Create a post for user with id 1 with post_content as my first post
...
Q5="Write your query here"
...
Write a query to get all users in User table.
...
Q6="Write your query here"
...
Write a query to get first_name and last_name of all users from User table
...
Q7="Write your query here"
...

Write a query to update Tony stark name to
first_name = thor
last name = ragnarok
...
Q8="Write your query here"
...

Write a query to create a post user with id 2 with “My Second Post” as post_content
...
Q9="Write your query here"
...

Delete John wick in User table
...
Q10="Write your query here"
...

Delete the post table
...
Q11="Write your query here"
...

---------------------------------------------------------------------------------------------------------------------------------


Q1='''CREATE TABLE User(
        user_id INT PRIMARY KEY NOT NULL,
        first_name  VARCHAR(200) NOT NULL,
        last_name VARCHAR(200) NOT NULL,
        address VARCHAR(300),
        phone_number  INT  NOT NULL);'''
Q2='''CREATE TABLE Post(
        user_id INT,
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_content VARCHAR(500)
                );'''
Q3='''INSERT INTO User(user_id,first_name,last_name,address,phone_number) 
    values(1,'tony','stark','new york',1234567890);'''
    
Q4='''INSERT INTO User(user_id,first_name,last_name,address,phone_number) values(2,'john','wick','la',987654321);'''
    
Q5='''INSERT INTO Post(user_id,post_content) 
      values(1,'my first post');'''
      
Q6='SELECT * FROM User;'
Q7='SELECT first_name,last_name FROM User;'
Q8='''UPDATE User SET first_name='thor',last_name='ragnarok'
    where user_id=1;'''
Q9='''INSERT INTO Post(user_id,post_content) 
      values(2,'my second post');'''
Q10='DELETE FROM User where user_id=2;'
Q11='DROP TABLE Post'
        
        
        
        
        
        







       
