from Mapping.Interface.map_pb2 import MapFragment
from People.Interface.move_pb2 import UpdatedPosition, MovementRequest

def parse(serialized_bytes):
    req = MovementRequest()
    req.ParseFromString(serialized_bytes)
    if req.type == "MovementRequest":
        return req
    elif req.type == "UpdatedPosition":
        req = UpdatedPosition()
        req.ParseFromString(serialized_bytes)
        return req
    elif req.type == "MapFragment":
        req = MapFragment()
        req.ParseFromString(serialized_bytes)
    else:
        return None
