''' Pyspark Template file '''
import sys
from pyspark.sql import SparkSession

if len(sys.argv) != 3:
    print ('Usage: spark-submit ' + sys.argv[0] + ' <appName> <master_node>')
    sys.exit(1)

appName = sys.argv[1]
master = sys.argv[2]

# Setup SparkConf and SparkContext

try:
    ss = SparkSession.builder.appName(appName).master(master).getOrCreate()
    print ('Started app ' + appName + ' with master ' + master)
except:
    print ('Error creating SparkSession')
    sys.exit(1)

''' Do what you need here '''

''' Stop the SparkContext'''
ss.stop()

print ("Spark session closed.")
