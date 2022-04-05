# Import the pyspark.sql.types library
from pyspark.sql.types import *
from pyspark.sql import SparkSession

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

# Define a new schema using the StructType method
people_schema = StructType([
  # Define a StructField for each field
  StructField('name', StringType(), False),
  StructField('age', IntegerType(), False),
  StructField('city', StringType(), False)
])