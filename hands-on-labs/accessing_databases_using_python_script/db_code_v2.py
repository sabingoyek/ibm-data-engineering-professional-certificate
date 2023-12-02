import sqlite3
import pandas as pd

# 1-  Creating table Departments

db_name = "STAFF.db"
table_name = 'Departments'
attributes_list = ["DEPT_ID", "DEP_NAME", "MANAGER_ID", "LOC_ID"]

# reading csv file
csv_file_path = "Departments.csv"

df = pd.read_csv(csv_file_path, names=attributes_list)
#print(df)

# 2- Populating the Departments table

conn = sqlite3.connect(db_name)

df.to_sql(table_name, conn, if_exists='replace', index=False)

# 3- Appending data to the Departments table

data_dict = {
    "DEPT_ID": [9], 
    "DEP_NAME": "Quality Assurance",
    "MANAGER_ID": 30010,
    "LOC_ID": "L0010"
}

df = pd.DataFrame(data_dict)
print(df)
df.to_sql(table_name, conn, if_exists='append', index=False)

# 4-a Viewing all entries from Departments table

query_statement = f'SELECT * FROM {table_name}'
df2 = pd.read_sql(query_statement, conn)
print(df2)

# 4-b Viewing only the department name

query_statement = f'SELECT DEP_NAME from {table_name}'
df = pd.read_sql(query_statement, conn)
print(df)

# 4-b Counting the total entries

query_statement = f'SELECT COUNT(*) FROM {table_name}'
df = pd.read_sql(query_statement, conn)
print(df)

