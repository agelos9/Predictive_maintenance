# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 15:28:08 2022

@author: aggelosuser
"""
#!pip install paho.mqtt
import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("P#####")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    receiveTime=datetime.datetime.now()
    message=msg.payload.decode("utf-8")
    if "DOING_WELL" in message:
       print(message)
       my_list = message.split('},')
       for i in my_list:
           if "TRSC" in i:
              continue
           timestamp = i[(i.find("timestamp")+12) : (i.find("signalId")-3)]
           signal = i[(i.find("signalId")+11) : (i.find("value") -3)]
           value = i[(i.find("value")+7) : (i.find("qBit")-2)]

           post={"time":timestamp,"signal":signal,"value":value}
           collection.insert_one(post)
    #print(msg.topic+" "+str(msg.payload))

if __name__ == "__main__":
    mongoClient=MongoClient()
    db=mongoClient.SensorData
    collection=db.home_data3

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    #client.connect("192.168.1.50", 1883, 60)
    client.connect("10.250.100.240",1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()