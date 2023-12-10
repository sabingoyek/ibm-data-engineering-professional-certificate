# Final project of Python Project for Data Engineering course: Acquiring and Processing Information on the World's Largest Banks


## Project Scenario

A multi-national firm has hired you as a data engineer. Your job is to access and process data as per requirements.

Your boss asked you to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, you need to transform the data and store it in USD, GBP, EUR, and INR per the exchange rate information made available to you as a CSV file. You should save the processed information table locally in a CSV format and as a database table. Managers from different countries will query the database table to extract the list and note the market capitalization value in their own currency.

Your job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

Particulars of the code to be made have been shared below.

Parameter	Value
Code name	banks_project.py
Data URL	https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks
Exchange rate CSV path	https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
Table Attributes (upon Extraction only)	Name, MC_USD_Billion
Table Attributes (final)	Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion
Output CSV Path	./Largest_banks_data.csv
Database name	Banks.db
Table name	Largest_banks
Log file	code_log.txt

## Directions

- Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.
- Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
- Write a function to load the transformed data frame to an output CSV file.
- Write a function to load the transformed data frame to an SQL database server as a table.
- Write a function to run queries on the database table.
- Run the following queries on the database table:
    a. Extract the information for the London office, that is Name and MC_GBP_Billion
    b. Extract the information for the Berlin office, that is Name and MC_EUR_Billion
    c. Extract the information for New Delhi office, that is Name and MC_INR_Billion
- Write a function to log the progress of the code.
- While executing the data initialization commands and function calls, maintain appropriate log entries.