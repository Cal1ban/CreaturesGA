import asyncio
import websockets
from Mapping.move_pb2 import Direction, Movement
import json
from Mapping.Map import Map
import redis
from kafka import KafkaProducer


async def move(websocket, path):
    input = await websocket.recv()
    movement = Movement()
    movement.ParseFromString(input.encode("utf-8"))
    new_pos = Map(conn, movement.slug).move(movement.direction)
    producer.send("movement", input.encode("utf-8"))
    await websocket.send(",".join([str(x) for x in new_pos]))

async def on_connect(ws):
    print("Connected")

conn = redis.StrictRedis(host = 'localhost', port=6379) 
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

start_server = websockets.serve(move, 'localhost', 5000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()