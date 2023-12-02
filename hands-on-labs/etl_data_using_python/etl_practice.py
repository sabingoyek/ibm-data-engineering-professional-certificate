import glob
import pandas as pd
from xml.etree import ElementTree as ET
from datetime import datetime

from utils import extract_from_csv, extract_from_json, load_data, log_progress, etl

log_file = "practice_data/log_file.txt"
target_file = "practice_data/transformed_data.csv"
cols = ["car_model", "year_of_manufacture", "price", "fuel"]

#df = extract_from_csv("practice_data/used_car_prices1.csv")
#print(df)

#df = extract_from_json("practice_data/used_car_prices1.json")
#print(df)

def extract_from_xml(file_to_process):
    df = pd.DataFrame(columns=cols)
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        df = pd.concat([df, 
                        pd.DataFrame(
                            [{"car_model": car_model, 
                              "year_of_manufacture": year_of_manufacture, 
                              "price": price, 
                              "fuel": fuel}]
                        )])
    return df

#df = extract_from_xml("practice_data/used_car_prices1.xml")
#print(df)


def extract():
    extracted_data = pd.DataFrame(columns=cols) # create an empty dataframe to hold extracted data

    # process all csv files
    for csvfile in glob.glob("practice_data/*.csv"):
        new_df = pd.DataFrame(extract_from_csv(csvfile))
        extracted_data = pd.concat([extracted_data, new_df], ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("practice_data/*.json"):
        new_df = pd.DataFrame(extract_from_json(jsonfile))
        extracted_data = pd.concat([extracted_data, new_df], ignore_index=True)

    # process xml files
    for xmlfile in glob.glob("practice_data/*.xml"):
        new_df = pd.DataFrame(extract_from_xml(xmlfile))
        extracted_data = pd.concat([extracted_data, new_df], ignore_index=True)

    return extracted_data

#df = extract()
#print(df)

# Task 2: Transformation

def transform(data):
    '''Round off to two decimals price column '''
    data['price'] = round(data.price, 2)

    return data

#df = transform(df)
#print(df)

# Testing ETL operations and log progress

etl(extract, transform, load_data, target_file, log_file)