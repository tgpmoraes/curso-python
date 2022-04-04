from pyspark.sql import SparkSession

spark = (SparkSession.builder.getOrCreate())
spark.sparkContext.setLogLevel("ERROR")

file_path = "../dataset/people.csv"

# Create an DataFrame from file_path
people_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Create a temporary table "people"
people_df.createOrReplaceTempView("people")

# Filter the people table to select female sex 
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')

# Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')

# Count the number of rows in both DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames"
    .format(people_female_df.count(), people_male_df.count()))