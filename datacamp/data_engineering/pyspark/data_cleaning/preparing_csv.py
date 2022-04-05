from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path = "../dataset/2018.csv"

# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(Header=True).load(file_path)

aa_dfw_df = aa_dfw_df. \
    filter(aa_dfw_df.OP_CARRIER == 'AA'). \
    filter(aa_dfw_df.ORIGIN == 'DFW'). \
    select('FL_DATE', 'OP_CARRIER_FL_NUM', 'DEST', 'ACTUAL_ELAPSED_TIME')

aa_dfw_df.write.parquet('../dataset/AA_DFW_2018.parquet', mode='overwrite')