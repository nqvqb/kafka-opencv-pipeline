# Kafka OpenCV Pipeline


##### kafka-python
```sh
# create a topic
/home/kafka/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
# check if the topic is created
/home/kafka/kafka/bin/kafka-topics.sh --list --zookeeper lhost:2181
# describe the topic 
/home/kafka/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic testTopic
# returns:
# Topic:testTopic	PartitionCount:1	ReplicationFactor:1	Configs:
# 	Topic: testTopic	Partition: 0	Leader: 0	Replicas: 0	Isr: 0

virtualenv --system-site-packages -p python3 ~/kafka-opencv-pipeline/venv/kafka
source ~/kafka-opencv-pipeline/venv/kafka/bin/activate
pip install kafka-python
```

##### Test consumer and producer
```sh
/home/kafka/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
/home/kafka/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181
/home/kafka/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic testTopic
source ~/kafka-opencv-pipeline/venv/kafka/bin/activate
```