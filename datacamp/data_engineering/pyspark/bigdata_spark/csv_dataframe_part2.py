from pyspark.sql import SparkSession

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path = "../dataset/Fifa2018_dataset.csv"

# Load the Dataframe
fifa_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

# Construct the "query"
query = '''SELECT Age FROM fifa_df_table WHERE Nationality == "Germany"'''

# Apply the SQL "query"
fifa_df_germany_age = spark.sql(query)

# Generate basic statistics
fifa_df_germany_age.describe().show()