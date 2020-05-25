

class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass
class Student:
    
    def __init__(self,name,age, score):
        self.student_id = None
        self.name = name
        self.age = age
        self.score = score
    
    @classmethod
    def get(cls,**kid):
        
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
                                
       
        for k,v in kid.items():
           a=k
           b=v

        col=["student_id","name","age","score"]  
        if a not in col:
            raise InvalidField
        if a == 'name':
            sql_query="select * from Student where {}=\'{}\'".format(a,b) 
        else:
            sql_query="select * from Student where {}={}".format(a,b) 
        
        crsr.execute(sql_query) 
        ans=crsr.fetchall()

        if len(ans)==0:
            raise DoesNotExist
        if len(ans)>1:
            raise MultipleObjectsReturned

        obj=Student(ans[0][1],ans[0][2],ans[0][3])
        obj.student_id=ans[0][0]
        conn.close()
        return obj
        
    def delete(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;") 
        sql_query="Delete FROM Student where student_id={}".format(self.student_id)
        crsr.execute(sql_query) 
        conn.commit()
        conn.close()
    
    
    def save(self):
        import sqlite3
        conn=sqlite3.connect("students.sqlite3")
        crsr=conn.cursor()
        crsr.execute("PRAGMA foreign_keys=on;") 
        if self.student_id!=None:
            sql_query="UPDATE Student SET name='{}',age={},score={} where student_id={};".format(self.name,self.age,self.score,self.student_id)
            crsr.execute(sql_query) 
        else:
            sql_query="INSERT INTO Student(name,age,score) values('{}',{},{})".format(self.name,self.age,self.score)
            crsr.execute(sql_query) 
            self.student_id=crsr.lastrowid
        conn.commit()
        conn.close


#student_object = Student.get(score=100)
#print(student_object.name)

__________________________________________________________________________________________________________________
Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_012. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_012/
#Coding Guidelines
Write your code in student.py
# Problem Statement
A Student has name, age, score and student_id attributes, Where student_id value is unique for each student object.

Student class for the above mentioned details:

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    ...


In order to persist student details in the database. We need the following methods to create, retrieve, update and delete student data in the database.

get
save
delete
filter
# Task1:
Implement get method as mentioned in the above description. get method is used to retrieve a student from the database for a give condition and returns a Student object with the details retrieved from the database.

# Data in Table
student_id	name	age	score
1	Raj	20	100
2	Vivek	21	90
3	Roshan	19	100
# Example
>>> student_object = Student.get(student_id=1)
>>> student_object.student_id
1
>>> student_object.name
Raj
>>> student_object.age
20
>>> student_object.score
100
If there are no results that match the given condition, get() should raise DoesNotExist exception.
# Example
>>> student_object = Student.get(student_id=100)
DoesNotExist:
...
If there are more than one student that match the given condition, get() should raise MultipleObjectsReturned exception.
# Example
>>> student_object = Student.get(score=100)
MultipleObjectsReturned:
...

It should raise an InvalidField if you are trying to fetch student details using fields other than student_id, name, age and score.
# Example
>>> student_object = Student.get(some_random_field=100)
InvalidField:
...
# Task2:
Used to delete the given object from the database
# Data in Table
student_id	name	age	score
1	Raj	20	100
2	Vivek	21	90
3	Roshan	19	100
# Example
>>> student_object = Student.get(student_id=1)
>>> student_object.delete()
# Data in Table
student_id	name	age	score
2	Vivek	21	90
3	Roshan	19	100
# Task3 - update:
save method creates or updates a student object in database
# Data in Table
student_id	name	age	score
1	Raj	20	100
2	Vivek	21	90
3	Roshan	19	100
# Example
>>> student_object = Student.get(student_id=1)
>>> student_object.name = "Suresh"
>>> student_object.save()
# Data in Table
student_id	name	age	score
1	Suresh	20	100
2	Vivek	21	90
3	Roshan	19	100
If you have noticed name of the entry in student table with student_id=1 is updated.
# Task3 - create:
create method can be used to create a new entry in the database.

# Example
>>> student_object = Student(name="Rajini", age=19, score=95)
>>> student_object.save()
# Data in Table
student_id	name	age	score
1	Suresh	20	100
2	Vivek	21	90
3	Roshan	19	100
4	Rajini	19	95
If you have noticed, a new entry in student table has been created.
Saving and already existing object in database shouldn't create a new entry in database.
# Example
>>> student_object = Student.get(student_id=4)
>>> student_object.save()
The above code doesn't create an entry in the database.
# Learning Material
Sample python snippets to execute SQL queries.
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

Reference to access sqlite3 database using python.
Note: Test cases for your submissions are executed on students.sqlite3 database with Student table created using the below SQL query.

CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(250),
    age INT,
    score INT
);
Learn defining custom exceptions in Python in this reference







