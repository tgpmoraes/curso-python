from pyspark.sql.types import *
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path = "../dataset/AA_DFW_2017_Departures_Short.csv.gz"

# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(Header=True).load(file_path)

# Add the airport column using the F.lower() method
aa_dfw_df = aa_dfw_df.withColumn('airport', F.lower(aa_dfw_df['Destination Airport']))

# Drop the Destination Airport column
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])

# Show the DataFrame
aa_dfw_df.show()