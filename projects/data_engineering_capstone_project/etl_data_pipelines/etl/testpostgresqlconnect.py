# This program requires the python module ibm-db to be installed.
# Install it using the below command
# python3 -m pip install psycopg2

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


PG_USER=os.getenv("PG_USER")
PG_HOST=os.getenv("PG_HOST")
PG_PWD=os.getenv("PG_PWD")

# connectction details
 
dsn_database ="softCart" 

# create connection

conn = psycopg2.connect(
   database=dsn_database, 
   user=PG_USER,
   password=PG_PWD,
   host=PG_HOST
)

print("Connected successfully")

cursor = conn.cursor()

q = "select max(row_id) from sales_data"

cursor.execute(query=q)
rs = cursor.fetchall()
last_row_id = rs[0][0]
print(last_row_id)

conn.close()