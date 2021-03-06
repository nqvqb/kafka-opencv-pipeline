# Kafka and OpenCV Image processing pipeline


## Install Apache Kafka on Ubuntu18

##### References
1. https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-18-04
2. https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-an-apache-zookeeper-cluster-on-ubuntu-18-04
3. https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-18-04#installing-specific-versions-of-openjdk
4. https://stackoverflow.com/questions/33537950/how-to-delete-a-topic-in-apache-kafka

##### Prerequisites
1. ubuntu18
2. at least 4GB of RAM
3. OpenJDK8
4. Zookeeper

##### Setup Kafka user
As kafka is running as a system service and via network ports, it is better to separate it as different user in case kafka is compomised
```sh
# create user
# login as non root another user, then create user with home dir
sudo useradd kafka -m
# add passworkd
sudo passwd kafka
# add kafka user to sudo
sudo adduser kafka sudo
# set bash as the default shell for the kafka user
sudo usermod --shell /bin/bash kafka
```
##### Download
Download kafaka and install java sdk 8
```sh
su -l kafka
mkdir ~/Downloads
curl "https://www.apache.org/dist/kafka/2.1.1/kafka_2.11-2.1.1.tgz" -o ~/Downloads/kafka.tgz
curl "https://www.apache.org/dist/kafka/2.3.1/kafka_2.11-2.3.1.tgz" -o ~/Downloads/kafka.tgz
mkdir ~/kafka && cd ~/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1
# install OpenJDK8
sudo apt install openjdk-8-jdk
# verification OpenJDK8
java -version
```
##### Config kafka server

```sh
sudo gedit ~/kafka/config/server.properties
```
```diff
+	delete.topic.enable = true
```
##### Creating systemd unit file and start zookeeper
```diff
sudo gedit /etc/systemd/system/zookeeper.service
+	[Unit]
+	Requires=network.target remote-fs.target
+	After=network.target remote-fs.target
+	
+	[Service]
+	Type=simple
+	User=kafka
+	ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties
+	ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
+	Restart=on-abnormal
+	
+	[Install]
+	WantedBy=multi-user.target
```
##### Create systemd unit file for kafka.service
```diff
sudo gedit /etc/systemd/system/kafka.service
+	[Unit]
+	Requires=zookeeper.service
+	After=zookeeper.service
+	
+	[Service]
+	Type=simple
+	User=kafka
+	ExecStart=/bin/sh -c '/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties > /home/kafka/kafka/kafka.log 2>&1'
+	ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
+	Restart=on-abnormal
+	
+	[Install]
+	WantedBy=multi-user.target
```
##### Start service
```sh
sudo systemctl start kafka
sudo journalctl -u kafka
# enable reboot
sudo systemctl enable kafka
```
##### (optional) disable service if want to remove kafka
```sh
sudo systemctl is-active kafka
sudo systemctl stop kafka
sudo systemctl disable kafka
sudo rm /etc/systemd/system/kafka.service
sudo systemctl daemon-reload

sudo systemctl is-active zookeeper
sudo systemctl stop zookeeper
sudo systemctl disable zookeeper
sudo rm /etc/systemd/system/zookeeper.service
sudo systemctl daemon-reload

# remove kafka user 
sudo su -
# deregister user
sudo userdel kafka
sudo userdel -r kafka
# remove all kafka home
sudo rm -r /home/kafka
sudo reboot
```
##### Test kafka publisher and and consumer
```sh
# login as kafka
# create a topic called testTopic
~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
/home/kafka/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic
# publish a topic called kafka
echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic > /dev/null
echo "Hello, World" | /home/kafka/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic > /dev/null

# consume
# -from-beginning flag: allows the consumption of messages that were published before the consumer was started
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testTopic --from-beginning
/home/kafka/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testTopic --from-beginning
# this node is always running, keep consuming if new message comes in
# login as kafka in another terminal
# publish the topic again
echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic > /dev/null
```
##### Running in localhost
sometimes kafka dident work properly in localhost, uncomment the 2 lines in server.properties:
```sh
listeners=PLAINTEXT://localhost:9092
advertised.listeners=PLAINTEXT://localhost:9092
```
##### Delete a topic
Apache Kafka never deletes a topic marked for deletion if that topic has producers still producing to it, or consumers still consuming from it, or messages left hanging out in the queue. 
One way to force it is to restart Kafka. 
```sh
# login as kafka
# set delete.topic.enable to true
# list all topic
~/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181
/home/kafka/kafka/bin/kafka-topics.sh --list --zookeeper localhost:2181
# delete one 
~/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic testTopic
/home/kafka/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic testTopic
```

##### Remove all Java
```sh
# remove the links, alternatives 
sudo update-alternatives --remove "java"
sudo update-alternatives --remove "javac"
sudo update-alternatives --remove "javaws"
# remove packages
sudo rm -r /usr/lib/jvm/jdk[version]
# uninstall openjdk
# remove jdk only
sudo apt-get remove openjdk*
# remove jdk along with dependencies
sudo apt-get remove --auto-remove openjdk*
# remove jdk with configs
sudo apt-get purge openjdk*
# remove configs, dependencies
sudo apt-get purge --auto-remove openjdk*
```









































































