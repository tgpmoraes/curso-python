from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path = "../dataset/people.csv"

# Create an DataFrame from file_path
people_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Create a temporary table "people"
people_df.createOrReplaceTempView("people")

# Construct a query to select the names of the people from the temporary table "people"
query = '''SELECT name, 2022 - INT(SUBSTR(`date of birth`, 1, 4))  AS age FROM people'''

# Assign the result of Spark's query to people_df_names
people_df_names = spark.sql(query)

names_df = people_df_names.withColumnRenamed('name', 'Name') \
                          .withColumnRenamed('age', 'Age')

# Check the column names of names_df
print("The column names of names_df are", names_df.columns)

# Convert to Pandas DataFrame  
df_pandas = names_df.toPandas()

# Create a horizontal bar plot
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()