from Mapping.Square import Square
from Mapping.Terrain import Terrain, create_terrain_distribution
from random import choice
from typing import Iterable
import itertools
from time import sleep


class Map:
    def __init__(self, grid):
        self.grid = grid
        self.max_coordinate = len(self.grid) - 1
        self.add_distributions()

    def get_area_around_coordinate(self, x_pos, y_pos, distance):
        min_x = max(0, x_pos - distance)
        max_x = min(self.max_coordinate, x_pos + distance)
        min_y = max(0, y_pos - distance)
        max_y = min(self.max_coordinate, y_pos + distance)

        x_positions = range(min_x, max_x + 1)
        y_positions = range(min_y, max_y + 1)
        coords = list(itertools.product(x_positions, y_positions))
        return [self.grid[x[0]][x[1]] for x in coords]

    def add_distributions(self):
        for row in self.grid:
            for col in row:
                col.surrounding_terrain = create_terrain_distribution(
                    self.get_area_around_coordinate(col.x_pos, col.y_pos, 2))

    def get_regions(self):
        output = {}
        for row in self.grid:
            for col in row:
                if col.region in output:
                    output[col.region].append(col)
                else:
                    output[col.region] = [col]
        return output

    def display(self):
        for row in self.grid:
            print(",".join([str(x.region) for x in row]))
        print("----")


def manhatten_distance(first_square: Square, second_square: Square) -> int:
    return abs(first_square.x_pos - second_square.x_pos) + abs(first_square.y_pos - second_square.y_pos)
