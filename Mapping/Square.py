from Mapping.Interface.map_pb2 import Terrain


class Square:

    def __init__(self, x_pos, y_pos, terrain : Terrain):
        self.x_pos, self.y_pos, self.terrain = x_pos, y_pos, terrain
        self.region = None
        self.surrounding_terrain = None
    def assign_region(self, region):
        self.region = region
