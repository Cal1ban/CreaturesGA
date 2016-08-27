from kafka import KafkaConsumer, KafkaProducer
from People.Interface.move import UpdatedPosition
from Utilities.Serialization.serialize import serialize

consumer = KafkaConsumer('main', bootstrap_servers=['0.0.0.0:9092'])
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

messageOne = UpdatedPosition()
messageOne.x_pos = 3
messageOne.y_pos = 3
messageOne.p_id = 10

producer.send("fe", serialize(messageOne))