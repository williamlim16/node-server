import paho.mqtt.client as mqtt
import time

mqttBroker = "127.0.0.1"
client = mqtt.Client("testing")
client.connect(mqttBroker)

while True:
    client.publish("TESTING2", "mint")
    print("just published testing")
    time.sleep(3)
