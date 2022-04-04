from pyspark.context import SparkContext


sc = SparkContext('local', 'test')
sc.setLogLevel("WARN")

numbRDD = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create map() transformation to cube numbers
cubedRDD = numbRDD.map(lambda x: x ** 3)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
	print(numb)