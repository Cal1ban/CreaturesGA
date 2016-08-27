#!/usr/bin/env python

import asyncio
import websockets


from kafka import KafkaConsumer, KafkaProducer

consumer = KafkaConsumer('movement', bootstrap_servers=['0.0.0.0:9092'])
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

def message_generator():
    for message in consumer:
        yield message.value

async def mapping_broker(websocket, path):
    name = await websocket.recv()
    msg = next(gens)
    print(msg)
    await websocket.send(msg)

gens = message_generator()

start_server = websockets.serve(mapping_broker, 'localhost', 5000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
