
from kafka import KafkaConsumer

consumer = KafkaConsumer('testTopic')
for message in consumer:
    print (message)