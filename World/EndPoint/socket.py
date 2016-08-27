import asyncio
import websockets
from People.Interface.move_pb2 import Movement
from Kafka import KafkaProducer

async def world_gateway(websocket, path):
    input = await websocket.recv()
    movement = Movement()
    movement.ParseFromString(input)

    p_id = movement.p_id

    #Record the move into history
    producer.send("movement", movement)

    #Request more map
    

    update = pos_repo.make_move()
    await websocket.send(update.SerializeToString())

##Client says move this way
##Back end says sure and here's some more world

async def on_connect(ws):
    print("Connected")

pos_repo = PositionRepository()
producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
start_server = register_movement.serve(world_portal, 'localhost', 5001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()