#!/bin/bash

echo "extract_transform_and_load"
cut -d":" -f1,3,6 /etc/passwd > ~/airflow/data/extracted-data-for-shell-dag.txt

tr ":" "," < ~/airflow/data/extracted-data-for-shell-dag.txt > ~/airflow/data/transformed-data-for-shell-dag.csv
