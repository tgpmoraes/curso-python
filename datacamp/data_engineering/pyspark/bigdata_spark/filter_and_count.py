from pyspark.context import SparkContext

file_path = "../dataset/airports.csv"

sc = SparkContext('local', 'test')
sc.setLogLevel("WARN")
# Load a local file into PySpark shell
fileRDD = sc.textFile(file_path)

# Filter the fileRDD to select lines with Spark keyword
fileRDD_filter = fileRDD.filter(lambda line: 'Atlantic' in line)

# How many lines are there in fileRDD?
print("The total number of lines with the keyword Spark is", fileRDD_filter.count())

# Print the first four lines of fileRDD
for line in fileRDD_filter.take(4): 
  print(line)
