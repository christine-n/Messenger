#!/usr/bin/env python
import pika
import json

def publish(message):
    print("Start Producer")
    credentials = pika.PlainCredentials(username='admin', password='982020')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='172.19.0.1', port=5675, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    )
    channel.basic_publish(exchange='', routing_key='task_queue', body=json.dumps(message), properties=properties)
    print(" [x] Sent %r" % message)
    connection.close()
    return
