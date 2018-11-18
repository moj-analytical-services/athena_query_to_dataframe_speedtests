## Datasets held in csv format have a sql interface 

library(odbc)
con <- dbConnect(odbc::odbc(), "Athena")
sql <-  "
select * from 
flights_demo.flights_raw
limit 10000000
"

start.time <- Sys.time()


df <- odbc::dbGetQuery(con, sql)
end.time <- Sys.time()
time.taken <- end.time - start.time
time.taken

