from pyspark.context import SparkContext

file_path = "../dataset/airports.csv"

sc = SparkContext('local', 'test')
sc.setLogLevel("WARN")
# Load a local file into PySpark shell
fileRDD = sc.textFile(file_path)

# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(file_path, minPartitions = 5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is", fileRDD_part.getNumPartitions())