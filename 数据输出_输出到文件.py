from pyspark import SparkConf,SparkContext
import os

os.environ['HADOOP_HOME'] = "D:\hadoop-3.0.0"
os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1,2,3,4,5],numSlices=1)
rdd2 = sc.parallelize([("Hello",3),("Spark",5),("Hi",7)],numSlices=1)
rdd3 = sc.parallelize([[1,3,5],[6,7,9],[11,13,11]],numSlices=1)

rdd1.saveAsTextFile("D:/output1")
rdd2.saveAsTextFile("D:/output2")
rdd3.saveAsTextFile("D:/output3")