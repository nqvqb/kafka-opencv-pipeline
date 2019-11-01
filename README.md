# Kafka OpenCV Pipeline
##### Test consumer and producer
/home/kafka/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
/home/kafka/kafka/bin/kafka-topics.sh --list --zookeeper lhost:2181
/home/kafka/kafka/bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic testTopic
source ~/kafka-opencv-pipeline/venv/kafka/bin/activate
