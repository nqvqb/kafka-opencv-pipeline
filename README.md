# Kafka OpenCV Pipeline

## Install OpenCV
##### References
1. https://docs.opencv.org/4.0.0/d7/d9f/tutorial_linux_install.html
2. https://opencv.org/opencv-4-0/
##### Download and compile
```sh
# remove apt installed opencv
sudo apt remove opencv
# clone latest branch from git source
git clone --single-branch --branch 4.1.2 git@github.com:opencv/opencv.git
# compile opencv
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# git clone opencv
# the opencv must be at home dir?
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
# https://blog.csdn.net/orDream/article/details/84311697
# make
make -j7
cd ~/opencv/build/doc/
make -j7 doxygen

sudo make install
```
##### Test opencv
```sh
sudo apt install virtualenv -y
sudo apt-get install python-pip -y
sudo apt-get install python3-pip -y
sudo apt-get install ffmpeg -y
virtualenv --system-site-packages -p python3 ~/kafka-opencv-pipeline/venv/test
source ~/kafka-opencv-pipeline/venv/test/bin/activate
```
## Network debug
##### ZooKeeper
```sh
# ZooKeeper will kick of automatically as a daemon set to port 2181
netstat -ant | grep :2181
```

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
start simple consumer and producer
```sh
cd ~/kafka-opencv-pipeline
python3 test_producer.py

# open another terminial
source ~/kafka-opencv-pipeline/venv/kafka/bin/activate
python3 test_consumer.py
```


