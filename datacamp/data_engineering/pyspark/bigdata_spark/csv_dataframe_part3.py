from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

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

# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()