import attr
from enum import Enum


class Terrain(Enum):
    UNKNOWN = 0
    GRASS = 1
    RIVER = 2
    SEA = 3
    MOUNTAIN = 4
    PLAIN = 5


@attr.s
class Cell:
    terrain = attr.ib(validator=attr.validators.instance_of(Terrain))
    x_pos = attr.ib(validator=attr.validators.instance_of(int))
    y_pos = attr.ib(validator=attr.validators.instance_of(int))


@attr.s
class MapFragment:
    id = attr.ib()
    cells = attr.ib()
