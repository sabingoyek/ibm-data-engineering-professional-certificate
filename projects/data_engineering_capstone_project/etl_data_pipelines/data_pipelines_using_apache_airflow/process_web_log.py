# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

dag_args = {
    'owner': 'Kimba SABI N\'GOYE',
    'start_date': days_ago(0),
    'email': ['test@test.com']
}

# defining the DAG
dag = DAG(
    'process_web_log',
    default_args=dag_args,
    description='ETL on Web Server log DAG',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# extract task: extract the ipaddress field

extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d" " -f1 $AIRFLOW_HOME/data/accesslog.txt > $AIRFLOW_HOME/data/extracted_data.txt',
    dag=dag,
)

# transform task: filter out all the occurrences of ipaddress “198.46.149.143” from extracted_data.txt 
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep 198.46.149.143 $AIRFLOW_HOME/data/extracted_data.txt > $AIRFLOW_HOME/data/transformed_data.txt',
    dag=dag,
)

# load task: archive the file transformed_data.txt into a tar file named weblog.tar
load_data = BashOperator(
        task_id='load_data',
        bash_command='cd $AIRFLOW_HOME/data/ && tar -cvf weblog.tar transformed_data.txt',
        dag=dag
)

# task pipeline
extract_data >> transform_data >> load_data


