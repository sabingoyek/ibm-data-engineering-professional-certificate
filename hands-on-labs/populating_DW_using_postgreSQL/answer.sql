-- find the count of rows in the table FactBilling
SELECT COUNT(*) FROM public."FactBilling";

-- create a simple MQT named avg_customer_bill with fields customerid and averagebillamount.
CREATE MATERIALIZED VIEW avg_customer_bill (customerid, averagebillamount) AS
(SELECT customerid, AVG(billedamount) FROM public."FactBilling" GROUP BY customerid);

-- Refresh the newly created MQT
REFRESH MATERIALIZED VIEW avg_customer_bill;


-- Using the newly created MQT find the customers whose average billing is more than 11000
select * from avg_customer_bill where averagebillamount > 11000;



