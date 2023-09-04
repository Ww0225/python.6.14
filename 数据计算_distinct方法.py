from pyspark import SparkConf,SparkContext
import os


os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,1,3,3,5,5,7,7])
rdd1 = rdd.distinct()
print(rdd1.collect())