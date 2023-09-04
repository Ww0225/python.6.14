from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_pys_map")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["ww ","py ","666 "])

rdd1 = rdd.flatMap(lambda x : x.split(" "))
print(rdd1.collect())