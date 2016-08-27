from random import choice
from typing import Iterable
from Mapping.Interface.map_pb2 import Cell, Terrain, Row, Map, RIVER, SEA
import redis

class MapFactory:  

    def create_random_map_data(self, size):
        mappy = Map()
        for x in range(size):
            row = Row()
            for y in range(size):
                cell = Cell()
                cell.x_pos = x
                cell.y_pos = y
                cell.terrain = self.choose_random_terrain()
                row.cells.extend([cell])
            mappy.rows.extend([row])
        return mappy

    def choose_random_terrain(self):
        return choice(list(Terrain.values()))

    def create_river_map(self):
        mappy = Map()
        for x in range(10):
            row = Row()
            for y in range(10):
                if x < 2 and y < 2:
                    cell = Cell()
                    cell.x_pos = x
                    cell.y_pos = y
                    cell.terrain = RIVER
                    row.cells.extend([cell])
                else:
                    cell = Cell()
                    cell.x_pos = x
                    cell.y_pos = y
                    cell.terrain = SEA
                    row.cells.extend([cell])
            mappy.rows.extend([row])
        return self.store_new_map(mappy)