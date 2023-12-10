#!/bin/bash

DATA_DIR=${AIRFLOW_HOME}/dags/data

SCRIPTS_DIR=${AIRFLOW_HOME}/scripts

FILE_URL='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt'

wget $FILE_URL -P $DATA_DIR/

cut -d"#" -f1,4 $DATA_DIR/web-server-access-log.txt > $DATA_DIR/extracted.txt

tr "[a-z]" "[A-Z]" < $DATA_DIR/extracted.txt > $DATA_DIR/capitalized.txt

tar -cvf $DATA_DIR/log.tar.gz $DATA_DIR/capitalized.txt
