# This program requires the python module mysql-connector-python to be installed.
# Install it using the below command
# pip3 install mysql-connector-python

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_HOST=os.getenv("MYSQL_HOST")
MYSQL_PWD=os.getenv("MYSQL_PWD")

#print(MYSQL_PWD)

# connect to database
connection = mysql.connector.connect(user=MYSQL_USER, host=MYSQL_HOST, password=MYSQL_PWD, database='sales')

print("Connected successfully")
mysql_cursor = connection.cursor()
rowid = 12289

query = f"SELECT * FROM sales_data WHERE rowid > {rowid}"
mysql_cursor.execute(query)
rows = mysql_cursor.fetchall()

print(rows)

# close connection
connection.close()
