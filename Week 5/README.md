# Python module for SQL
The psycopg2 module in Python allows us to make SQL queries through Python. In this basically a cursor object is defined and a query written as a String is executed. After this the data obtained is fetched using cursor.fetchall() to get the data in the form of a list. 
Execution can be found in the .py file in PYSQL folder
# Median using NumPy in SQL
In the Median folder, a python script is there to find out median of a column in a database using psycopg2 and numpy.median(). This is a much better approach as we cannot directly find out median using purely SQL. 
We can also use the binapprox algorithm if our database is large.
# Additional Ideas
We can actually do much more using the psycopg2 module. Databases have now become an integral part of the Backend. So, the psycopg2 module can act as a bridge between the SQL databases and the various ML ALgortihms like DTC and Random Forest.
