from dataclasses import dataclass

from smart_snakes.game.directions.absolute_direction import AbsoluteDirection


@dataclass
class Point:
    x: int
    y: int

    def get_point_in_direction(self, direction: AbsoluteDirection):
        match direction:
            case AbsoluteDirection.UP:
                return Point(self.x, self.y - 1)
            case AbsoluteDirection.LEFT:
                return Point(self.x - 1, self.y)
            case AbsoluteDirection.DOWN:
                return Point(self.x, self.y + 1)
            case AbsoluteDirection.RIGHT:
                return Point(self.x + 1, self.y)
