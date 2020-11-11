#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import pika
import json
#import config as cfg

# Connect to RabbitMQ and create channel
credentials = pika.PlainCredentials('guest', 'CTOsO65A6QRcuozmavJCuoia')
parameters = pika.ConnectionParameters('127.0.0.1', 5673, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare and listen queue
channel.queue_declare(queue='my_queue')


# Function process and print data
def callback(ch, method, properties, body):
    print("Method: {}".format(method))
    print("Properties: {}".format(properties))
    data = json.loads(body)
    print("ID: {}".format(data['id']))
    print("Name: {}".format(data['name']))
    print('Description: {}'.format(data['description']))

#Listen and receive data from queue
channel.basic_consume(queue='my_queue',auto_ack=True, on_message_callback=callback)
channel.start_consuming()


