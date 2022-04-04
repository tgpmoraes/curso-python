from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = (SparkSession.builder.getOrCreate())

df = spark.read.csv('dataset/flights_small.csv', header=True)
df.createOrReplaceTempView("flights")

# Create the DataFrame flights
flights = spark.table("flights")

flights = flights.withColumn("distance",
                             flights.distance.cast("int")) \
                 .withColumn("air_time",
                             flights.air_time.cast("int"))

# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()