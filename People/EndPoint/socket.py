import asyncio
import websockets
from People.Storage import PositionRepository
from People.Interface.move_pb2 import UpdatedPosition


async def get_position(websocket, path):
    input = await websocket.recv()
    p_id = int(input.encode("utf-8"))
    position = pos_repo.get_pos(p_id)
    pos = UpdatedPosition()
    pos.p_id = p_id
    pos.x_pos = position.x_pos
    pos.y_pos = position.y_pos

    await websocket.send(pos.SerializeToString())


async def on_connect(ws):
    print("Connected")


pos_repo = PositionRepository()
start_server = register_movement.serve(get_position, 'localhost', 5001)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
