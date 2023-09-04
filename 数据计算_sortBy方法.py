from pyspark import SparkConf,SparkContext
import os


os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.textFile("D:\word.txt")

word_rdd = rdd.flatMap(lambda x: x.split(" "))

word_with_onw_rdd = word_rdd.map(lambda word: (word,1))

result_rdd = word_with_onw_rdd.reduceByKey(lambda a,b:a+b)

final_rdd = result_rdd.sortBy(lambda x: x[1],ascending=True,numPartitions=1)

print(final_rdd.collect())