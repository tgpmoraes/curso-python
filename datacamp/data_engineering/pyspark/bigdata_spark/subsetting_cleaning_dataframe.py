from pyspark.sql import SparkSession

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path = "../dataset/people.csv"

# Create an DataFrame from file_path
people_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Select name, sex and date of birth columns
people_df_sub = people_df.select('name', 'sex', 'date of birth')

# Print the first 10 observations from people_df_sub
people_df_sub.show(10)

# Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates"
    .format(people_df_sub.count(), people_df_sub_nodup.count()))