# Project Overview

## Instructions
Now that you are equipped with the knowledge and skills to work with several different NoSQL databases you have the opportunity in the final project to practice and apply your skills by working with different databases to move and analyze data.

## Scenario
You are a data engineer at a Data Analytics Consulting Company. Your company prides itself in being able to efficiently handle data in any format on any database on any platform. Analysts in the offices need to work with data on different databases, and with data in different formats. While they are good at analyzing data, they count on you to be able to move data from external sources into various databases, move data from one type of database to another, and be able to run basic queries on various databases.

## Objectives
- replicate a Cloudant database.
- create indexes on a Cloudant database.
- query data in a Cloudant database.
- import data into a MongoDB database.
- query data in a MongoDB database.
- export data from MongoDB.
- import data into a Cassandra database.
- query data in a Cassandra database.

## Tasks

1- Replicate a remote database into your Cloudant instance.
2- Create an index for key "director", on the database movies using the HTTP API.
3- Write a query to find all movies directed by Richard Gage using the HTTP API.
4- Create an index for key "title", on the database movies using the HTTP API.
5- Write a query to list only the keys year and director for the movie `Top Dog` using the HTTP API.
6- Export the data from movies database into a file named movies.json. 
7- Import movies.json into mongodb server into a database named entertainment and collection named movies.
8- Write a mongodb query to find the year in which most number of movies were released.
9- Write a mongodb query to find the count of movies released after the year 1999.
10- Write a query to find out the average votes for movies released in 2007.
11- Export the fields _id, title, year, rating and director from movies collection into a file named partial_data.csv.
12- Import partial_data.csv into cassandra server into a keyspace named entertainment and table named movies.
13- Write a cql query to count the number of rows in the movies table.
14- Create an index for the column rating in the movies table using cql.
15- Write a cql query to count the number of in the movies that are rated 'G'.


