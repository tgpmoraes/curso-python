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

# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()