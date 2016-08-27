from kafka import KafkaProducer
from People.Storage.PositionCache import PositionCache
from People.Interface.move import MovementRequest
from Mapping.Interface.map import Terrain
from Utilities.Stream.Stream import start_stream

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
pos_repo = PositionCache()


def store_into_cache(movement):
    if movement.destination.terrain == Terrain.MOUNTAIN:
        print("Blocked by mountain")
        return
    new_pos = pos_repo.update_position(movement)
    print("new pos", new_pos)
    producer.send("position", new_pos.SerializeToString())


start_stream("main", store_into_cache, [MovementRequest])
