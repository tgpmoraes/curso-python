from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path_2017 = "../dataset/AA_DFW_2017_Departures_Short.csv.gz"
file_path_2018 = "../dataset/AA_DFW_2018.parquet/*"

df1 = spark.read.format('csv'). \
    options(Header=True). \
    load(file_path_2017). \
    withColumnRenamed('Date (MM/DD/YYYY)', 'FL_DATE'). \
    withColumnRenamed('Flight Number', 'OP_CARRIER_FL_NUM'). \
    withColumnRenamed('Destination Airport', 'DEST'). \
    withColumnRenamed('Actual elapsed time (Minutes)', 'ACTUAL_ELAPSED_TIME')

df2 = spark.read.parquet(file_path_2018)

# View the row count of df1 and df2
print("df1 Count: %d" % df1.count())
print("df2 Count: %d" % df2.count())

# Combine the DataFrames into one
df3 = df1.union(df2)

# Save the df3 DataFrame in Parquet format
df3.write.parquet('../dataset/AA_DFW_ALL.parquet', mode='overwrite')

# Read the Parquet file into a new DataFrame and run a count
print(spark.read.parquet('../dataset/AA_DFW_ALL.parquet').count())