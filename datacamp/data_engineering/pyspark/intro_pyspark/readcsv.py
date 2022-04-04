from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = (SparkSession.builder.getOrCreate())

# Don't change this file path
file_path = "dataset/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()