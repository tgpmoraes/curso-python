from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = (SparkSession.builder.getOrCreate())

df = spark.read.csv('dataset/flights_small.csv', header=True)
df.createOrReplaceTempView("flights")
print(spark.catalog.listTables())

# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())