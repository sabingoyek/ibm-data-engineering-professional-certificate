# My Initial Design

## Dimension tables
 
- MyDimDate: 
	- dateid
	- day
	- weekday
	- weekdayname
	- month
	- monthname
	- quarter
	- quartername
	- year

	
- MyDimWaste
	- wasteid
	- wastetype
	- quantity
	
- MyDimZone
	- zoneid
	- zone
	- city	

## Fact table
- MyFactTrips
	- tripid
	- trucktype
	- truckid
	- zoneid
	- wasteid
	- dateid
