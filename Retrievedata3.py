Retrieving data from a table - String Comparison
In this reference, you will learn how to perform basic string operations like startswith, endswith, contains. We use LIKE and % for this purpose (which are detailed in the below sections).

# Startswith
To fetch records with an attribute cloumn1 value starting with the given value we write the below SQL query.

# Syntax
SELECT * FROM {table_name} WHERE column1 LIKE '{value}%'     
# Example
sqlite> SELECT name FROM Student WHERE name LIKE 'Er%';

# Explanation
The above query will fetch the name of all the records from Student table whose name attribute value starts with "Er"

# Result
Erik Alexander
# Try it yourself
Write an SQL query to fetch first_name attribute of all the records from Employee table whose first_name starts with "al"
# Expected Output
 Alex
 Allan
 Alex
 Alex
 Alberta
 Allan
 Alejandro
 Alfred
# Endswith
To fetch records with an attribute cloumn1 value ending with the given value we write the below SQL query.

# Syntax
SELECT * FROM {table_name} WHERE column1 LIKE '%{value}'     
# Example
sqlite> SELECT name FROM Student WHERE name LIKE '%ok';

Above SQL query returns name attribute of all the records from Student table whose name ends with "ok".

# Result
Jonathan Westbrook
# Try it yourself
Write an SQL query to fetch all the records from Employee table whose first_name ends with "mas"
# Expected Output
 117|Thomas|Dickinson|25|68039
 261|Thomas|Tamborlane|32|37591
 425|Thomas|Johnson|19|94028
 486|Thomas|Whipple|36|41386
# Contains
To fetch records with an attribute cloumn1 value containing the given value we write the below SQL query.

# Syntax
SELECT * FROM table_name WHERE column LIKE '%XXXX%'     
# Example
sqlite> SELECT name FROM Student WHERE name LIKE '%Eri%';

Above SQL query returns name attribute of all the records from Student table whose name contains "Eri".

# Result
Erik Alexander
Catherine Weatherford
# Try it yourself
Write a query to select all records from Employee table where first_name contains all
# Expected Output
64|Allan|Weir|32|28796
278|Allan|Black|40|28209
354|Hallie|Percell|29|95442
472|Marshall|Cullum|37|83494
