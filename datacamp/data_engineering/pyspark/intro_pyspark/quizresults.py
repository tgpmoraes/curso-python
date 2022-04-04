from pyspark.sql import SparkSession
from pyspark.sql.functions import *


spark = (SparkSession.builder.getOrCreate())


quizresults = spark.read.json('dataset/quizresults.json')

winner = quizresults.orderBy(desc("Points")).first()

spark.createDataFrame([winner]).show()


spark.stop()
