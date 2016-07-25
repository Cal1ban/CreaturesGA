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
            return False
        else:
            min_distance = min([manhatten_distance(region_square, square) for region_square in region.squares])
            return min_distance == 1

    regions = []
    region_id = 1

    for row in world_map.grid:
        for col in row:
            for region in regions:
                if point_in_region(region, col):
                    region.squares.append(col)
                    col.region = region_id
                    break
            else:
                regions.append(Region(world_map, [col]))
                region_id += 1
                col.region = region_id
    return world_map


def modify_regions(world_map: Map):
    regions = world_map.get_regions()
    region_distributions = {}
    for region in regions:
        sqs = regions[region]
        region_dist = average_distribution([x.surrounding_terrain for x in sqs])
        region_distributions[region] = region_dist
    for region in region_distributions:
        print(region, region_distributions[region].normalized_weights())
    update = False
    for row in world_map.grid:
        for col in row:
            dist = col.surrounding_terrain
            print(dist.normalized_weights())
            surrounding_squares = [x for x in world_map.get_area_around_coordinate(col.x_pos, col.y_pos, 1)]
            #print(surrounding_squares)
            surrounding_regions = [x.region for x in surrounding_squares]
            #print(surrounding_regions)
            surrounding_distributions = [region_distributions[x] for x in surrounding_regions]
            distances = [x.difference_to_distribution(dist) for x in surrounding_distributions]
            print(distances)
            print([x.normalized_weights() for x in surrounding_distributions])
            min_index = min(enumerate(distances), key=itemgetter(1))[0]
            print(surrounding_regions)
            print(min_index)

            new_region = surrounding_regions[min_index]
            print(new_region, col.region)
            if new_region != col.region:
                update = True
            col.region = new_region

    return update, world_map



