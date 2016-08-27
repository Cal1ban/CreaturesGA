from Mapping.Terrain import Terrain
from random import choice
from Mapping.Interface.map import MapFragment, Terrain, Cell
from People.Interface.move import UpdatedPosition


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
            cell = Cell()
            cell.terrain = terrain
            frag = MapFragment()
            frag.cells.extend([cell])
            return frag
