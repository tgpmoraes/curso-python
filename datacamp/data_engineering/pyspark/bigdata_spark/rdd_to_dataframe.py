from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local', 'test')
sc.setLogLevel("WARN")
spark = (SparkSession.builder.getOrCreate())

sample_list = [('Mona', 20), ('Jennifer', 34), ('John', 20), ('Jim', 26)]

# Create an RDD from the list
rdd = sc.parallelize(sample_list)

# Create a PySpark DataFrame
names_df = spark.createDataFrame(rdd, schema=['Name', 'Age'])

# Check the type of names_df
print("The type of names_df is", type(names_df))