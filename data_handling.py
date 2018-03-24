import sys
from faker import Factory

# Spark Imports
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

if len(sys.argv) != 3:
    print ('Usage: spark-submit ' + sys.argv[0] + ' <appName> <master_node>')
    sys.exit(1)

appName = sys.argv[1]
master = sys.argv[2]

# Create SparkSession. This creates SparkContext as well.

try:
    ss = SparkSession.builder.appName(appName).master(master).getOrCreate()
    print ('Started app ' + appName + ' with master ' + master)
except:
    print ('Error creating SparkSession')
    sys.exit(1)

# Creating a dataframe

# From a Python collection (list etc.)
fake = Factory.create()
fake.seed(4321)

myData = []

def fake_entry():
      name = fake.name().split()
      return (name[1], name[0], fake.ssn(), fake.job(), abs(2016 - fake.date_time().year) + 1)

for _ in range(1,20):
    myData.append(fake_entry())

dataDF = ss.createDataFrame(myData, ('last_name', 'first_name', 'ssn', 'occupation', 'age'))

print ('')

print ("Created dataframe from random seed. The schema is \n")

dataDF.printSchema()

print ("Here are a few entries \n")

for row in dataDF.take(5):
    print row

print ("\nNumber of dataframe partitions = " + str(dataDF.rdd.getNumPartitions()))

''' Stop the SparkContext'''
ss.stop()

print ("Spark session closed.")
