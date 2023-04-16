#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:24:01 2023

@author: marlafuente
"""

from paho.mqtt.client import Client

from time import sleep
from numpy import random

def main(broker):
    client = Client()

    client.connect(broker)
    client.loop_start()
    
    print('Publishing')

    while True:
        t = random.randint(0,8)
        data= f'[espera:{t},topic: /clients/{t},message: hello to {t}]'    
        client.publish('/clients/tempoMar',  data)
        print('.', end= '', flush=True)
        sleep(1)


if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        print(f"Usage: {sys.argv[0]}")
    broker = 'simba.fdi.ucm.es'
    main(broker)