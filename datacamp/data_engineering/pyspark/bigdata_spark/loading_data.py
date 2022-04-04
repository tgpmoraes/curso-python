from pyspark.context import SparkContext

file_path = "../dataset/airports.csv"

sc = SparkContext('local', 'test')
sc.setLogLevel("WARN")
# Load a local file into PySpark shell
lines = sc.textFile(file_path)
print(lines.collect())
