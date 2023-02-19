import unittest

from smart_snakes.game.directions.absolute_direction import AbsoluteDirection
from smart_snakes.game.directions.relative_direction import RelativeDirection


class TestAbsoluteDirection(unittest.TestCase):

    # noinspection DuplicatedCode
    def test_relative(self):

        # UP
        self.assertEqual(AbsoluteDirection.UP.relative(RelativeDirection.AHEAD), AbsoluteDirection.UP)
        self.assertEqual(AbsoluteDirection.UP.relative(RelativeDirection.LEFT), AbsoluteDirection.LEFT)
        self.assertEqual(AbsoluteDirection.UP.relative(RelativeDirection.RIGHT), AbsoluteDirection.RIGHT)

        # LEFT
        self.assertEqual(AbsoluteDirection.LEFT.relative(RelativeDirection.AHEAD), AbsoluteDirection.LEFT)
        self.assertEqual(AbsoluteDirection.LEFT.relative(RelativeDirection.LEFT), AbsoluteDirection.DOWN)
        self.assertEqual(AbsoluteDirection.LEFT.relative(RelativeDirection.RIGHT), AbsoluteDirection.UP)

        # DOWN
        self.assertEqual(AbsoluteDirection.DOWN.relative(RelativeDirection.AHEAD), AbsoluteDirection.DOWN)
        self.assertEqual(AbsoluteDirection.DOWN.relative(RelativeDirection.LEFT), AbsoluteDirection.RIGHT)
        self.assertEqual(AbsoluteDirection.DOWN.relative(RelativeDirection.RIGHT), AbsoluteDirection.LEFT)

        # Right
        self.assertEqual(AbsoluteDirection.RIGHT.relative(RelativeDirection.AHEAD), AbsoluteDirection.RIGHT)
        self.assertEqual(AbsoluteDirection.RIGHT.relative(RelativeDirection.LEFT), AbsoluteDirection.UP)
        self.assertEqual(AbsoluteDirection.RIGHT.relative(RelativeDirection.RIGHT), AbsoluteDirection.DOWN)
