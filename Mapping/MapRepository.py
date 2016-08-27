from random import choice
from typing import Iterable
from Mapping.MapFactory import MapFactory
from Mapping.Map import Map
from People.Interface.move_pb2 import UpdatedPosition
from Mapping.Interface.map_pb2 import Cell, Terrain, Row, Map, RIVER, SEA, MapFragment
import redis


class MapRepository:
    def __init__(self, conn=redis.StrictRedis(host='localhost', port=6379), factory=MapFactory()):
        self.conn = conn
        self.factory = factory
        self.cache = {}

    def new_map(self):

        def generate_key(key, x, y):
            return "map:{0}:x:{1}:y:{2}".format(str(key), str(x), str(y))

        map = self.factory.create_random_map_data(10)
        map_id = self.conn.incr("map:id")
        for row in map.rows:
            for cell in row.cells:
                self.conn.set(generate_key(key, cell.x_pos, cell.y_pos), cell.terrain)
        return map_id

    def choose_random_terrain(self):
        return choice(list(Terrain.values()))

    def get_fragment(self, update: UpdatedPosition):
        terrain = self.conn.get("map:{0}:x:{1}:y:{2}".format(str(update.p_id), str(update.x_pos), str(update.y_pos)))
        print(terrain)
        if terrain is None:
            terrain = self.choose_random_terrain()
            self.conn.set("map:{0}:x:{1}:y:{2}".format(str(update.p_id), str(update.x_pos), str(update.y_pos)), terrain)
        else:
            terrain = int(terrain)
        print(terrain)
        cell = Cell()
        cell.x_pos = update.x_pos
        cell.y_pos = update.y_pos
        cell.terrain = terrain
        fragment = MapFragment()
        fragment.id = update.p_id
        fragment.cells.extend([cell])
        return fragment
