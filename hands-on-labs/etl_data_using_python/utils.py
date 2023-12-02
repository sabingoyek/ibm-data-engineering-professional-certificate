import pandas as pd
from datetime import datetime

# function to extract csv
def extract_from_csv(file_to_process):
    df = pd.read_csv(file_to_process)
    return df

#df = extract_from_csv("source1.csv")
#print(df)

# function to extract json
def extract_from_json(file_to_process):
    df = pd.read_json(file_to_process, lines=True)
    return df

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

def log_progress(message, log_file):
    timestamp_format = "%Y-%h-%d-%H:%M:%S" # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')

def etl(extract_func, transform_func, load_data_func, target_file, log_file):
    # Log the initialization of the ETL process
    log_progress("ETL Job Started", log_file)

    # Log the beginning of the Extraction process
    log_progress("Extract phase Started", log_file)
    extracted_data = extract_func()
    #print("Extracted data")
    #print(extracted_data)

    # Log the completition of the Extraction process
    log_progress("Extract phase Ended", log_file)

    # Log the beginning of the Transformation process
    log_progress("Transform phase Started", log_file)
    transformed_data = transform_func(extracted_data)
    #print("Transformed Data")
    #print(transformed_data)

    # Log the completition of the Transformation process
    log_progress("Transform phase Ended", log_file)

    # Log the beginning of the Loading process
    log_progress("Load phase started", log_file)
    load_data_func(target_file, transformed_data)

    # Log the completition of the Loading process
    log_progress("Load phase Ended", log_file)


    # Log the completition of the ETL process
    log_progress("ETL Job Ended", log_file)

