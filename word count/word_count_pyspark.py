from __future__ import print_function
from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.getOrCreate()

# sc = spark.sparkContext
# input_data_path = './data/news.csv'
# text_file = sc.textFile(input_data_path)
# counts = text_file.flatMap(lambda line: line.split(" ")) \
#     .map(lambda word: (word, 1)) \
#     .reduceByKey(lambda a, b: a + b)
# print(counts.collect())

df = spark.read.csv("./data/news.csv",header=True,sep=",");
df.printSchema
df.collect()[0][5]
