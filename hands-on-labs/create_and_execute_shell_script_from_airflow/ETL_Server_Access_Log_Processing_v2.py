# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Kimba SABI N\'GOYE',
    'start_date': days_ago(0),
    'email': ['snk@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_Server_Access_Log_Processing_v2',
    default_args=default_args,
    description='ETL Server Access Log Processing DAG',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# define download task

etl_v2 = BashOperator(
        task_id='ETL_v2',
        bash_command="~/airflow/dags/scripts/ETL_Server_Access_Log_Processing.sh ",
        dag=dag
)

# define task  pipeline

etl_v2
