import os
from dotenv import load_dotenv

# Import libraries required for connecting to mysql
import mysql.connector


# Import libraries required for connecting to DB2 or PostgreSql
import psycopg2

# Load env variables
load_dotenv()

# Connect to MySQL
MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_HOST=os.getenv("MYSQL_HOST")
MYSQL_PWD=os.getenv("MYSQL_PWD")

connection = mysql.connector.connect(user=MYSQL_USER, host=MYSQL_HOST, password=MYSQL_PWD, database='sales')

# create cursor

mysql_cursor = connection.cursor()

print("Connected successfully to MySQL server")


# Connect to DB2 or PostgreSql
PG_USER=os.getenv("PG_USER")
PG_HOST=os.getenv("PG_HOST")
PG_PWD=os.getenv("PG_PWD")

 
dsn_database ="softCart" 

# create connection

conn = psycopg2.connect(
   database=dsn_database, 
   user=PG_USER,
   password=PG_PWD,
   host=PG_HOST
)

# create cursor

pg_cursor = conn.cursor()

print("Connected successfully to postgresql server")


# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
	"""
	Returns the last rowid of the table sales_data on the sales_data table
	"""
	query = "SELECT MAX(rowid) FROM sales_data"
	pg_cursor.execute(query=query)
	result = pg_cursor.fetchall()
	return result[0][0]

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	"""
	Return a list of all records that have a rowid greater than the last_row_id in the sales_data table
	"""
	query = f"SELECT * FROM sales_data WHERE rowid > {rowid}"
	mysql_cursor.execute(query)
	rows = mysql_cursor.fetchall()
	return rows	

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
	for row in records:
		query = "INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES(%s,%s,%s,%s)"
		pg_cursor.execute(query, row)
		conn.commit()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
connection.close()

# disconnect from PostgreSql data warehouse 
conn.close()

# End of program