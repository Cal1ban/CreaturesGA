from People.Interface.move_pb2 import MovementRequest, UpdatedPosition
from Utilities.Stream.Stream import start_stream

start_stream("Parsing", lambda x: print(x), [MovementRequest])