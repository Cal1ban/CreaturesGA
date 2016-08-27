from People.Interface.move_pb2 import UpdatedPosition
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

update = UpdatedPosition()
update.p_id = 120
update.x_pos = 9
update.y_pos = 9

print(update)

producer.send("position", update.SerializeToString())