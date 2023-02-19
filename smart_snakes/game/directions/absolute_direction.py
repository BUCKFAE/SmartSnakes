from enum import Enum

from smart_snakes.game.directions.relative_direction import RelativeDirection


class AbsoluteDirection(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def relative(self, direction: RelativeDirection):
        return AbsoluteDirection((self.value + direction.value) % 4)
