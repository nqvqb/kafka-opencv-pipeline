
from kafka import KafkaConsumer

consumer = KafkaConsumer('testTopic')
print(consumer)
for message in consumer:
    print (message)