from enum import Enum


class Direction(Enum):
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


class CursorMode(Enum):
    EXITMODE = 1
    BOMBMODE = 2
    LINKMODE = 3


def mirror(direction):
    """
    Given a direction (i.e. a vector) returns the flipped direction
    :param direction: a direction to reverse
    :return: the input vector reversed completely
    """
    if direction == Direction.LEFT:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.LEFT
    if direction == Direction.UP:
        return Direction.DOWN
    if direction == Direction.DOWN:
        return Direction.UP
    return None
