#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:40:07 2023

@author: marlafuente
"""

from paho.mqtt.client import Client
import traceback
import sys

K0 = 5
K1 = 20

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    n = float (msg.payload)
    if msg.topic == 'temperature/t2':
        if n > K0 and userdata['humidity'] == 'd':
            client.subscribe('humidity')
            userdata['humidity'] = 's' 
        elif n < K0 and userdata['humidity'] == 's':
            client.unsubscribe('humidity') 
            userdata['humidity'] = 'd'
    elif msg.topic == 'humidity':
        if n > K1:
            client.unsubscribe('humidity')
            userdata['humidity'] = 'd'
            
def main(hostname):
    userdata = {
        'humidity': 'd'
    }
    client = Client(userdata= userdata)
    client.on_message = on_message

    print(f'Connecting on channels numbers on {hostname}')
    client.connect(hostname)

    client.subscribe('temperature/t2')

    client.loop_forever()

if __name__ == "__main__":
    if len(sys.argv)>1:
        print(f"Usage: {sys.argv[0]}")
    broker = 'simba.fdi.ucm.es'
    main(broker)