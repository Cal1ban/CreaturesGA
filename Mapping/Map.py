from Mapping.Square import Square
from Mapping.Terrain import Terrain, create_terrain_distribution
from random import choice
from typing import Iterable
import itertools
from time import sleep
from Mapping.Interface.map_pb2 import Map, MapFragment, Terrain
from People.Interface.move_pb2 import UpdatedPosition

class Map:
    def __init__(self, data):
        self.data = data
        self.id = self.data.id
        self.rows = []
        for row in self.data.rows:
            r = []
            for cell in row.cells:
                r.append(cell)
            self.rows.append(r)

    def get_map_fragment_for_cell(self, pos: UpdatedPosition):
        x, y = pos.x_pos, pos.y_pos
        try:
            cell = self.rows[x][y]
            frag = MapFragment()
            frag.cells.extend([cell])
            return frag
        except:
            terrain = choice(list(Terrain.values())) 
            cell = choice()
            frag = MapFragment()
            frag.cells.extend([cell])
            return frag
