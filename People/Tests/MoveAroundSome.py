from People.Interface.move_pb2 import Direction, Movement, LEFT,DOWN
from kafka import KafkaProducer
from time import sleep
import redis

conn = redis.StrictRedis(host = 'localhost', port=6379) 
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

print(conn.get("pos:120:x"))
print(conn.get("pos:120:y"))

mov = Movement()
mov.p_id = 120
mov.direction = DOWN
producer.send("movement", mov.SerializeToString())

sleep(1)
print(conn.get("pos:120:x"))
print(conn.get("pos:120:y"))
