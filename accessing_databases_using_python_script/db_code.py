import pandas as pd
import sqlite3

csv_path = "INSTRUCTOR.csv"
db_name = "STAFF.db"
table_name = "INSTRUCTORS"
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# read the csv file
df = pd.read_csv(csv_path, names=attribute_list)
#print(df)


# load the data into the database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
print("Table is ready")

# run some queries

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}

data_append = pd.DataFrame(data_dict)
#print(data_append)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()