from kafka import KafkaConsumer, KafkaClient, SimpleConsumer
from Mapping.move_pb2 import Movement
from Mapping.Map import Map
import redis

klient = KafkaClient("0.0.0.0:9092")
sc = SimpleConsumer(klient, "uniquse", "movement")
conn = redis.StrictRedis(host = 'localhost', port=6379) 

print(conn.get("pos:1:x"))
print(conn.get("pos:1:y"))

##1, 7

conn.set("pos:1:x", 0)
conn.set("pos:1:y", 0)

for message in sc:
    # try:
        print(message)
        movement = Movement()
        movement.ParseFromString(message.message.value)
        new_pos = Map(conn, movement.slug).move(movement.direction)
        print(new_pos)
    # except:
    #     pass

    