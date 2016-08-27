from enum import Enum
from itertools import groupby
from math import sqrt
from statistics import mean


class Terrain(Enum):
    river = 1
    sea = 2
    plain = 3
    mountain = 4


class TerrainDistribution:
    def __init__(self, river_count, sea_count, plain_count, mountain_count):
        self.river = river_count
        self.sea = sea_count
        self.plain = plain_count
        self.mountain = mountain_count

    def normalized_weights(self):
        values = [self.river, self.sea, self.plain, self.mountain]
        return [x / sum(values) for x in values]

    def difference_to_distribution(self, region):
        zipped = zip(self.normalized_weights(), region.normalized_weights())
        return sum([(x[0] - x[1]) ** 2 for x in zipped])


def create_terrain_distribution(squares):
    terrain_list = [x.terrain for x in squares]
    sea = len(list(filter(lambda x: x == Terrain.sea, terrain_list)))
    river = len(list(filter(lambda x: x == Terrain.river, terrain_list)))
    plain = len(list(filter(lambda x: x == Terrain.plain, terrain_list)))
    mountain = len(list(filter(lambda x: x == Terrain.mountain, terrain_list)))
    return TerrainDistribution(river, sea, plain, mountain)


def average_distribution(distributions):
    return TerrainDistribution(
        mean([x.normalized_weights()[0] for x in distributions]),
        mean([x.normalized_weights()[1] for x in distributions]),
        mean([x.normalized_weights()[2] for x in distributions]),
        mean([x.normalized_weights()[3] for x in distributions])
    )

def purity(region):
    return sqrt(region.difference_to_distribution(region))
