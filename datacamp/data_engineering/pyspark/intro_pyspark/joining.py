from pyspark.sql import SparkSession
import pyspark.sql.functions as F


spark = (SparkSession.builder.getOrCreate())

df = spark.read.csv('dataset/flights_small.csv', header=True)
df.createOrReplaceTempView("flights")

# Create the DataFrame flights
flights = spark.table("flights")

# Don't change this file path
file_path = "dataset/airports.csv"

# Read in the airports data
df2 = spark.read.csv(file_path, header=True)
df2.createOrReplaceTempView("airports")

# Create the DataFrame flights
airports = spark.table("airports")

# Examine the data
print(airports.show())

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")

# Examine the new DataFrame
print(flights_with_airports.show())
