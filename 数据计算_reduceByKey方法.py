from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_pys_map")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('a',1),('a',3),('b',5)])

rdd1 = rdd.reduceByKey(lambda a,b : a + b)
print(rdd1.collect())

sc.stop()
