# Spark Installation Quick Self-reference

## Intial Stuff

* First install java and scala
* Download spark zip file and extract to ```/usr/local```
* Make ```SPARK_HOME``` point to ```/usr/local/spark``` and add SPARK_HOME (prefix) to PATH
* Change owner of ```SPARK_HOME``` contents

## Configurations

The main configuration file is ```$SPARK_HOME/conf/spark-env.sh```

## Running Spark with default settings

```sbin/start-master.sh --webui-port 23333``` starts the master node at port 7078 and can be seen at hostname:23333

```sbin/start-slave.sh --master spark://hostname:7078 ``` will start slave and connect it to master

```spark-submit --master spark://hostname:7078 <python script> <arguments>``` will start app with the workers as configured
