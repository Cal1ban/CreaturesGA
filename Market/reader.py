import redis
from kafka import KafkaConsumer, KafkaClient
import flask
from message_pb2 import Message
from Market.commodities_pb2 import Commodity

conn = redis.StrictRedis(host = 'localhost', port=6379)   

def get_type_of_message(message):
    return message.ListFields()[0][0].name

client = KafkaClient(hosts=['0.0.0.0:9092'])
client.ensure_topic_exists('resource')


consumer = KafkaConsumer('resource', bootstrap_servers=['0.0.0.0:9092'])
for message in consumer:
    print(message)
    mess = Message()
    mess.ParseFromString(message.value)
    if get_type_of_message(mess) == "trade":
        user_a, user_b = mess.trade.user_a_id, mess.trade.user_b_id
        amount = mess.trade.amount

        conn.incr("user:" + str(user_a), int(amount))
        conn.decr("user:" + str(user_b), int(amount))
