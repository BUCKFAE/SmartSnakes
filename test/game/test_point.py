import unittest

from smart_snakes.game.directions.absolute_direction import AbsoluteDirection
from smart_snakes.game.point import Point


class TestPoint(unittest.TestCase):

    def test_to_symbol(self):
        self.assertEqual(Point(2, 1), Point(1, 1).get_point_in_direction(AbsoluteDirection.RIGHT))
        self.assertEqual(Point(0, 1), Point(1, 1).get_point_in_direction(AbsoluteDirection.LEFT))
        self.assertEqual(Point(1, 2), Point(1, 1).get_point_in_direction(AbsoluteDirection.DOWN))
        self.assertEqual(Point(1, 0), Point(1, 1).get_point_in_direction(AbsoluteDirection.UP))
