from Mapping.Map import Map
from Mapping.Square import Square
from typing import List, Callable
from Mapping.Map import manhatten_distance
import itertools
from Mapping.Terrain import create_terrain_distribution, average_distribution, TerrainDistribution
from operator import itemgetter

class Region:
    def __init__(self, world, squares):
        self.squares = squares
        self.world = world


def square_in_region(region, square):
    return any([x.x_pos == square.x_pos and x.y_pos == square.y_pos for x in region.squares])


def add_core_regions_to_map(world_map: Map) -> Map:
    def point_in_region(region: Region, square: Square) -> bool:
        if not square.terrain == region.squares[0].terrain:
            print(False)
            return False
        else:
            min_distance = min([manhatten_distance(region_square, square) for region_square in region.squares])
            print(min_distance)
            return min_distance == 1

    regions = []

    for row in world_map.grid:
        for col in row:
            for ii, region in enumerate(regions):
                if point_in_region(region, col):
                    region.squares.append(col)
                    col.region = ii
                    break
            else:
                regions.append(Region(world_map, [col]))
                col.region = len(regions) - 1
    return world_map


def modify_regions(world_map: Map):
    regions = world_map.get_regions()
    region_distributions = {}
    for region in regions:
        sqs = regions[region]
        region_dist = average_distribution([x.surrounding_terrain for x in sqs])
        region_distributions[region] = region_dist
    update = False
    for row in world_map.grid:
        for col in row:
            dist = col.surrounding_terrain
            surrounding_squares = [x for x in world_map.get_area_around_coordinate(col.x_pos, col.y_pos, 1)]
            surrounding_regions = [x.region for x in surrounding_squares]
            surrounding_distributions = [region_distributions[x] for x in surrounding_regions]
            distances = [x.difference_to_distribution(dist) for x in surrounding_distributions]
            min_index = min(enumerate(distances), key=itemgetter(1))[0]
            new_region = surrounding_regions[min_index]
            if new_region != col.region:
                update = True
            col.region = new_region

    return update, world_map



