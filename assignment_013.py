Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_013. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_013/
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
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)

    ...

Make use of the above code snippet.

In order to persist student details in the database. We need the following methods to create, retrieve, update and delete student data in the database.

get
save
delete
filter
In the previous assignment you have implemented get, save, and delete methods.

In this assignment you will be implementing the filter method. The limitation with the get method is that it can fetch only one object at a time. The filter method is used to fetch all the student objects from the database which matches a given condition.

You should write code to support the following conditional operations

Equals
Less Than
Less Than Or Equal To
Greater Than
Greater Than Or Equal To
Not Equal To
In
Contains
# Data in Table
student_id	name	age	score
1	Maude Vanhorne	23	89
2	Sarah Kirwan	34	44
3	Fletcher Lomago	40	7
4	Jesse Couch	34	62
5	Israel Gilliland	38	77
6	Michael Aguas	34	87
7	Stephen Boone	25	39
# Task1 - Equals:
We use = to mention an equals to condition.

# Example
>>> selected_students = Student.filter(age=40)
>>> selected_students
[Student(student_id=3, name=Fletcher Lomago, age=40, score=7)]
It should raise an InvalidField if you are trying to fetch student details using fields other than student_id, name, age, score and the possible lookups. Eg: score__gt
# Example
>>> Student.filter(year=80)
InvalidField
... 
It should return an empty list if no records matched with the given condition.
# Example
>>> Student.filter(age=100)
[]
It should return student objects from database if multiple conditions match the given condition.
# Example
>>> selected_students = Student.filter(age=34, name="Jesse Couch")
>>> selected_students
[Student(student_id=4, name=Jesse Couch, age=34, score=62)]
Implement a filter method so that the above operation, fetches all the student objects whose age is 34 and name is "Jesse Couch".

# Task2 - Less Than:
We use __lt along with the field to mention a less than condition.

# Example
>>> selected_students = Student.filter(age__lt=30)
>>> selected_students
[Student(student_id=1, name=Maude Vanhorne, age=23, score=89), Student(student_id=7, name=Stephen Boone, age=25, score=39)]
Implement a filter method so that the above operation, fetches all the student objects whose age is less than 30.

# Task3 - Less Than Or Equal To:
We use __lte along with the field to mention a less than or equal to condition.

# Example
>>> selected_students = Student.filter(age__lte=30)
>>> selected_students
[Student(student_id=1, name=Maude Vanhorne, age=23, score=89), Student(student_id=7, name=Stephen Boone, age=25, score=39)]
Implement a filter method so that the above operation, fetches all the student objects whose age is less than or equal to 30.

# Task4 - Greater Than:
We use __gt along with the field to mention a greater than condition.

# Example
>>> selected_students = Student.filter(score__gt=80)
>>> selected_students
[Student(student_id=1, name=Maude Vanhorne, age=23, score=89), Student(student_id=6, name=Michael Aguas, age=34, score=87)]
Implement a filter method so that the above operation, fetches all the student objects whose score greater than 80.

# Task5 - Greater Than Or Equal To:
We use __gte along with the field to mention a greater than or equal to condition.

# Example
>>> selected_students = Student.filter(age__gte=40)
>>> selected_students
[Student(student_id=3, name=Fletcher Lomago, age=40, score=7)]
Implement a filter method so that the above operation, fetches all the student objects whose age greater than or equal to 40.

# Task6 - Not Equal To:
We use __neq along with the field to mention a not equal to condition.

# Example
>>> selected_students = Student.filter(age__neq=34)
>>> selected_students
[Student(student_id=1, name=Maude Vanhorne, age=23, score=89), Student(student_id=3, name=Fletcher Lomago, age=40, score=7), Student(student_id=5, name=Israel Gilliland, age=38, score=77), Student(student_id=7, name=Stephen Boone, age=25, score=39)]
Implement a filter method so that the above operation, fetches all the student objects whose age not equal to 34.

# Task7 - In:
We use __in along with the field to mention in condition.

# Example
>>> ages = [25, 34]
>>> selected_students = Student.filter(age__in=ages)
>>> selected_students
[Student(student_id=2, name=Sarah Kirwan, age=34, score=44), Student(student_id=4, name=Jesse Couch, age=34, score=62), Student(student_id=6, name=Michael Aguas, age=34, score=87), Student(student_id=7, name=Stephen Boone, age=25, score=39)]
Implement a filter method so that the above operation, fetches all the student objects whose age is in given values i.e[25, 34] in the above example.

# Task8 - Contains:
We use __contains along with the field to mention contains condition.

>>> selected_students = Student.filter(name__contains='Jesse')
>>> selected_students
[Student(student_id=4, name=Jesse Couch, age=34, score=62)]
Implement a filter method so that the above operation, fetches all the student objects whose name contains Jesse.

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
Note: Test cases for your submissions are executed on selected_students.sqlite3 database with Student table created using the below SQL query.

CREATE TABLE Student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(250),
    age INT,
    score INT
);
Learn defining custom exceptions in Python in this reference
_________________________________________________________________________________________________________________________



Tests ran at 23 May 08 51 PM

42 tests passed out of 42 tests.

test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_student_id_return_student_object: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_age_return_student_object: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_score_return_student_object: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_name_return_student_object: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_age_when_multiple_objects_matched_raise_exception: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_invalid_student_id_raise_exception: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_invalid_age_raise_exception: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_invalid_score_raise_exception: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_invalid_name_raise_exception: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_get_method_given_invalid_column_field_raise_exception: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_delete_method_given_valid_student_id_deletes_record: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_save_method_given_record_does_not_present_in_db_then_create_record: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_save_method_given_record_present_in_db_then_update_record: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_save_method_given_updated_student_id_not_present_in_db_then_create_new_record: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_invalid_field_name: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_and_return_empty_list: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_multiple_conditions_and_return_empty_list: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_not_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_greater_than_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_less_than_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_greater_than_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_less_than_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_age_field_and_in_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_not_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_greater_than_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_less_than_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_greater_than_or_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_less_than_or_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_student_id_field_and_in_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_name_field_and_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_name_field_and_not_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_name_field_and_in_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_name_field_and_like_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_not_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_greater_than_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_less_than_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_greater_than_or_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_less_than_or_equal_operator: passed
test_75be180a-816d-43f3-a5d6-38d8fe09917a_db013.py::test_filtering_students_data_with_score_field_and_in_operator: passed


Errors: 0 errors


 
