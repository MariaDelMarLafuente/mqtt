#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:09:37 2023

@author: marlafuente
"""

from paho.mqtt.client import Client
import traceback
import sys
from sympy import isprime

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    try:
        frec = [0,0]
        n = float(msg.payload)
        if n != int(n):
            userdata['frecuenciaEnt'] += 1
            client.publish('/clients/realMar',msg.payload)
        else:
            userdata['frecuenciaReal'] += 1
            primo = isprime(int(n))
            data = f'{msg.payload} es primo: {primo}'
            client.publish('/clients/enterMar',data)
        client.publish('/clients/frecMar', f'{userdata}')
    except ValueError:
        pass
    except Exception as e:
        raise e


def main(broker):
    userdata = {'frecuenciaEnt':0, f'frecuenciaReal': 0}
    client = Client(userdata=userdata)
    client.on_message = on_message

    print(f'Connecting on channels numbers on {broker}')
    client.connect(broker)

    client.subscribe('numbers')

    client.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
