#! /bin/bash

echo "Stagging area setting up started"

echo "Creating bilingDW"

createdb -h localhost -U postgres -p 5432 billingDW

echo "bilingDW creation completed"

echo "Downloading and extracting scripts started"
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Setting%20up%20a%20staging%20area/billing-datawarehouse.tgz

tar -xvzf billing-datawarehouse.tgz

echo "Downloading and extracting scripts completed"

echo "Loading data into dimension table started"

psql  -h localhost -U postgres -p 5432 billingDW < DimCustomer.sql
psql  -h localhost -U postgres -p 5432 billingDW < DimMonth.sql
psql  -h localhost -U postgres -p 5432 billingDW < FactBilling.sql

echo "Loading data into dimension tables completed"

echo "Verification started"

psql  -h localhost -U postgres -p 5432 billingDW < verify.sql

echo "Verification completed"
