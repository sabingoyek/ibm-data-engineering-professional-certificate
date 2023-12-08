CREATE DATABASE sales;

CREATE TABLE sales_data(
	product_id INTEGER,
	customer_id INTEGER,
	price INTEGER,
	quantity INTEGER,
	timestamp TIMESTAMP
)

-- LOAD DATA FROM CSV FILE

-- LIST THE TABLES IN THE DATABASES sales
SHOW TABLES;

-- COUNT OF RECORDS IN THE TABLES sales_data
SELECT COUNT(*) FROM sales_data;

-- CREATE AN INDEX
CREATE INDEX ts ON sales_data.timestamp;

-- LIST INDEX
SHOW INDEX FROM sales_data;
