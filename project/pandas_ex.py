import os
import sys 
os.environ["SPARK_HOME"]="C:\Users\dy\Downloads\spark-2.0.0-bin-hadoop2.6\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder\
.master("local")\
.appName("myApp")\
.config(conf=myConf)\
.config('spark.sql.warehouse.dir','file:///C:/User/dy/Code/s_201311249/src')\
.getOrCreate()
import pandas as pd
df = pd.read_csv('example3.csv', delimiter=',')
df