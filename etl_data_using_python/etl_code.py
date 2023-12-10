import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime

from utils import extract_from_csv, extract_from_json, log_progress, load_data, etl

log_file = "lab_data/log_file.txt"
target_file = "lab_data/transformed_data.csv"


# Task 1: Extraction

#df = extract_from_csv("lab_data/source1.csv")
#print(df)


#df = extract_from_json("lab_data/source1.json")
#print(df)

# function to extract xml
def extract_from_xml(file_to_process):
    df = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        df = pd.concat([df, pd.DataFrame([{"name": name, "height": height, "weight": weight}])], ignore_index=True)
    return df

#df = extract_from_xml("lab_data/source1.xml")
#print(df)

def extract():
    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight']) # create an empty dataframe to hold extracted data

    # process all csv files
    for csvfile in glob.glob("lab_data/*.csv"):
        new_df = pd.DataFrame(extract_from_csv(csvfile))
        extracted_data = pd.concat([extracted_data, new_df], ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("lab_data/*.json"):
        new_df = pd.DataFrame(extract_from_json(jsonfile))
        extracted_data = pd.concat([extracted_data, new_df], ignore_index=True)

    # process xml files
    for xmlfile in glob.glob("lab_data/*.xml"):
        new_df = pd.DataFrame(extract_from_xml(xmlfile))
        extracted_data = pd.concat([extracted_data, new_df], ignore_index=True)

    return extracted_data

df = extract()
#print(df)


# Task 2: Transformation

def transform(data):
    '''Convert inches to meters and round off to two decimals
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254, 2)

    '''Convert pounds to kilograms and round off to the two decimals
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237)

    return data

df = transform(df)
#print(df)


#load_data(target_file, df)


# Testing ETL operations and log progress

etl(extract, transform, load_data, target_file, log_file)
