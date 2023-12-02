# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests
import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup


def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(LOG_FILE, "a") as f:
        f.write(timestamp + " : " + message + "\n")
    f.close()



def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    table = data.find_all("tbody")[0]
    rows = table.find_all("tr")[1:]
    data_dict = {
        "Name": [],
        "MC_USD_Billion": []
    }

    for row in rows:
        cols = row.find_all("td")
        name = str(cols[1].contents[2].text)
        mc = float(str(cols[2].text).strip())
        data_dict["Name"].append(name)
        data_dict["MC_USD_Billion"].append(mc)

    df = pd.DataFrame(data_dict)
    #print(df)

    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    exchange_rate = pd.read_csv(csv_path)
    exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]

    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]

    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]

    #print(df)

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(f"Query: {query_statement}")
    df = pd.read_sql(query_statement, sql_connection)
    print("Query result")
    print(df)

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"
DB_NAME = "Banks.db"
TABLE_NAME = "Largest_banks"
TABLE_INITIAL_ATTRIBUTES = ["Name", "MC_USD_Billion"] 
TABLE_FINAL_ATTRIBUTES = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
LOG_FILE = "code_log.txt"
TARGET_FILE = "Largest_banks_data.csv"
EXCHANGE_RATE_FILE = "exchange_rate.csv"

log_progress("Preliminaries complete. Initiating ETL process")

df = extract(URL, TABLE_INITIAL_ATTRIBUTES)

log_progress("Data extraction complete. Initiating Transformation process")


df = transform(df, EXCHANGE_RATE_FILE)
#print(df['MC_EUR_Billion'][4])

log_progress("Data transformation complete. Initiating Loading process")


load_to_csv(df, TARGET_FILE)
log_progress("Data saved to CSV file")

log_progress("SQL Connection initiated")

sql_connection = sqlite3.connect(DB_NAME)
load_to_db(df, sql_connection, TABLE_NAME)

log_progress("Data loaded to Database as a table, Executing queries")

query = "SELECT * FROM Largest_banks"
run_query(query, sql_connection)

query = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_query(query, sql_connection)

query = "SELECT Name from Largest_banks LIMIT 5"
run_query(query, sql_connection)

log_progress("Process Complete")

sql_connection.close()
log_progress("Server Connection closed")
