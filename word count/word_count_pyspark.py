from __future__ import print_function
from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct
from pyspark.sql.functions import *
from pyspark.sql.functions import split
import os

spark = SparkSession.builder.getOrCreate()

sc = spark.sparkContext
# input_data_path = './data/news.csv'
# text_file = sc.textFile(input_data_path)
# counts = text_file.map(lambda line: line.split(","))
# header = counts.take(1)[0]
# df = counts.filter(lambda x: x[0] != 'index').toDF(header)
# df.take(3)

df = spark.read.format('csv').option("escape","\"").option('header',True).load("./data/news.csv")
df.printSchema
df.collect()[0]

type(df)
df.show(1)
rdd = spark.read.format('csv').option("escape","\"").option('header',True).load("./data/news.csv").rdd
rdd.take(1)

type(rdd)

rdd.df = rdd.toDF()

rdd.df.take(1)

type(rdd.df)

# which means rdd.df & df are the same

rdd.df.select('text').show(1)

newdf = df.withColumn('text', regexp_replace('text', '\xa0', ''))
newdf = newdf.withColumn('text', regexp_replace('text', '\\\'', ''))


df.take(1)
newdf.take(1)

rdd_text = newdf.select('text').rdd
rdd_text.take(1)

counts_rdd = rdd_text.flatMap(lambda x: x[0].split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda x,y: x+y)
type(counts_rdd)
counts_rdd = counts_rdd.toDF('word','count')
