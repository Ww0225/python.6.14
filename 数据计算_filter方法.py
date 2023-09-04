from pyspark import SparkConf,SparkContext
import os


os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])
rdd1 = rdd.filter(lambda num: num % 2 == 0)
print(rdd1.collect())
