import attr
from Mapping.Interface.map import Cell


@attr.s
class MovementRequest:
    id = attr.ib()
    destination = attr.ib(validator=attr.validators.instance_of(Cell))


@attr.s
class UpdatedPosition:
    id = attr.ib()
    x_pos = attr.ib(validator=attr.validators.instance_of(int))
    y_pos = attr.ib(validator=attr.validators.instance_of(int))
