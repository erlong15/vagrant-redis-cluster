#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import pika
import json
#import config as cfg

# Connect to RabbitMQ and create channel
credentials = pika.PlainCredentials('guest', 'CTOsO65A6QRcuozmavJCuoia')

parameters = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# Declare queue to send data
channel.queue_declare(queue='my_queue')

data = {
    "id": 1,
    "name": "My Name",
    "description": "This is description about me"
}

message = json.dumps(data)

# Send data
res = channel.basic_publish(exchange='', routing_key='my_queue', body=message)
print(res)
print(" [x] Sent data to RabbitMQ")
connection.close()
