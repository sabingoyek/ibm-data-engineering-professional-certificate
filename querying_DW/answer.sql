-- grouping set for the columns year, quartername, sum(billedamount)
SELECT year, quartername, sum(billedamount) as billedamount
FROM "FactBilling"
LEFT JOIN "DimCustomer"
ON "FactBilling".customerid = "DimCustomer".customerid
LEFT JOIN "DimMonth"
ON "FactBilling".monthid="DimMonth".monthid
GROUP BY GROUPING SETS(year, quartername);


-- rollup for the columns country, category, sum(billedamount)
select year, quartername,  sum(billedamount) as totalbilledamount
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid="DimMonth".monthid
group by rollup(year, quartername)
order by year, quartername;

-- cube for the columns year,country, category, sum(billedamount)
select year, quartername, sum(billedamount) as totalbilledamount
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid="DimMonth".monthid
group by cube(year,quartername);

-- MQT named average_billamount with columns year, quarter, category, country, average_bill_amount
CREATE MATERIALIZED VIEW average_billamount(year, quarter, category, country, average_bill_amount) AS
(SELECT year, quarter, category, country,AVG(billedamount)
from "FactBilling"
left join "DimCustomer"
on "FactBilling".customerid = "DimCustomer".customerid
left join "DimMonth"
on "FactBilling".monthid="DimMonth".monthid
group by year,quarter,category,country);

REFRESH MATERIALIZED VIEW average_billamount;
