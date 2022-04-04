from pyspark.sql import SparkSession
import pyspark.sql.functions as F


spark = (SparkSession.builder.getOrCreate())

df = spark.read.csv('dataset/flights_small.csv', header=True)
df.createOrReplaceTempView("flights")

# Create the DataFrame flights
flights = spark.table("flights")

flights = flights.withColumn("dep_delay",
                             flights.distance.cast("int")) \
                 .withColumn("air_time",
                             flights.air_time.cast("int"))

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()
