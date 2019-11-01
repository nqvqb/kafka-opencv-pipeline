
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
print(producer)
producer.send('testTopic', b'Hello, World!')
producer.send('testTopic', key=b'message-two', value=b'This is Kafka-Python')