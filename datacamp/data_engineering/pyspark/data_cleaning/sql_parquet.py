from pyspark.sql import SparkSession

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

# Read the Parquet file into flights_df
flights_df = spark.read.parquet('../dataset/AA_DFW_ALL.parquet')

# Register the temp table
flights_df.createOrReplaceTempView('flights')

# Run a SQL query of the average flight duration
avg_duration = spark.sql('SELECT avg(ACTUAL_ELAPSED_TIME) from flights').collect()[0]
print('The average flight time is: %d' % avg_duration)