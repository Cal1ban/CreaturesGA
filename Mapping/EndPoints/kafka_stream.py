from kafka import KafkaConsumer, KafkaProducer
from People.Interface.move_pb2 import Movement, UpdatedPosition
from time import sleep
from Mapping.Interface.map_pb2 import MapFragment, Cell, RIVER
from Mapping.MapRepository import MapRepository

consumer = KafkaConsumer('position', bootstrap_servers=['0.0.0.0:9092'])
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
repo = MapRepository()

print("here")
for message in consumer:
    print(message)
    update = UpdatedPosition()
    update.ParseFromString(message.value)
    mappy = repo.get_fragment(update)
    print(mappy)
    producer.send("maps", mappy.SerializeToString())