# athena_query_to_dataframe_speedtests

This repo contains various code snippets that we've used to time the performance of data reads into pandas.

Specifically, we're interested in optimising reading sql query results into pandas dataframes.

In this repo we test various things:

- Reading from Athena using ODBC/JDBC drivers
- Reading from Athena by picking up the results from the .csv byproducts
- Performing a Create Table As and reding the results from parquet
- Comparison to reading from csv and parquet on disk
- Comparison to reading from a sqlite database on disk
- Comparison to reading from a RDS/postgres instance 



### Performance so far:



So….i’ve been using Athena’s `create table as` to get better performance of reading a sql query into pandas memory.  Once the apache arrow projects delivers parquet reads in R, we should be able to get the same benefits
by using `create table as` we get to choose our output format, so we can do query -> parquet dump in s3.  We can also choose the number of partitions (files).
we can then use `pyarrow` to read a folder of parquet files, increasing read performance
First results are reasonably good.  We can perform a query that returns a ~1.1Gb file (well, it’s 1.1Gb in csv format, the actual output is four smaller parquet files), and load that into a pandas dataframe.  The whole thing takes 19 seconds. (edited)
The parquet output has the advantage that we don’t need to worry about type conversion.

robinlinacre [3:58 PM]
Reading the same dataset from disk (SSD) as a `.csv` file on my Macbook pro takes 40 seconds.  As a `.parquet` takes 8 seconds. (edited)

robinlinacre [4:18 PM]
Timings of the same query in current version of dbtools: 117 seconds in Python and 230 seconds for R. (edited)
I think this means using this new method  we’re getting _much_ faster query performance than we would from a relational database. (edited)
