import flask
import redis
import json
from flask import request
from message_pb2 import Message
from kafka import KafkaProducer

app = flask.Flask(__name__)


@app.route('/market/user/<int:user_id>', methods=['GET'])
def user(user_id):
    amount = conn.get("user:" + str(user_id))
    print(amount)
    try:
        return json.dumps({"id": user_id, "amount": int(amount)})
    except TypeError:
        return json.dumps({"id": user_id, "amount": 0})


@app.route('/market/trade', methods=['POST'])
def trade():
    body = request.json
    user_a, user_b = body["user_a_id"], body["user_b_id"]
    print(user_a, user_b)
    amount = body["amount"]

    conn.incr("user:" + str(user_a), int(amount))
    conn.decr("user:" + str(user_b), int(amount))

    comm = Message()
    comm.trade.user_a_id = user_a
    comm.trade.user_b_id = user_b
    comm.trade.commodity_id = 1
    comm.trade.amount = amount

    producer.send("resource", comm.SerializeToString())

    return json.dumps({"status": "Success"})


if __name__ == '__main__':
    conn = redis.StrictRedis(host='localhost', port=6379)
    producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
    app.run(debug=True)
