from kafka import KafkaConsumer, KafkaProducer
from People.Storage.PositionCache import PositionCache
from People.Interface.move_pb2 import MovementRequest
from time import sleep
consumer = KafkaConsumer('movement', bootstrap_servers=['0.0.0.0:9092'])
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

pos_repo = PositionCache()

print("Here")

for message in consumer:
    movement = Movement()
    movement.ParseFromString(message.value)
    print(movement.direction)
    new_pos = pos_repo.update_position(movement)
    print(new_pos)
    producer.send("position", new_pos.SerializeToString())