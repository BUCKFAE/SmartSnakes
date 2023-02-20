import unittest

from smart_snakes.game.board import Board
from smart_snakes.game.directions.absolute_direction import AbsoluteDirection
from smart_snakes.game.directions.relative_direction import RelativeDirection
from smart_snakes.game.point import Point
from smart_snakes.game.tile import Tile
from smart_snakes.log.snake_logger import logger


class TestBoard(unittest.TestCase):

    def test_get_size(self):
        b1 = Board(7, 9, 2)
        self.assertEqual(b1.get_size(), (7, 9))

    def test_board_operations(self):
        b = Board(7, 9, 3)
        logger.info(f'Test board:\n{b}')

        # Snake only spawns in the 4th row
        for y in range(9):
            if y == 4:
                continue
            for x in range(7):
                # Tile is either food or empty
                self.assertTrue(b.get_tile(Point(x, y)).value <= 0)

        # Snake starts at tile (2, 4) and ends at (4, 4)
        self.assertEqual(b.get_tile(Point(2, 4)), Tile.BODY)
        self.assertEqual(b.get_tile(Point(3, 4)), Tile.BODY)
        self.assertEqual(b.get_tile(Point(4, 4)), Tile.HEAD)
        for x in [0, 1, 5, 6]:
            self.assertTrue(b.get_tile(Point(x, 4)) in [Tile.EMPTY, Tile.FOOD])

        # Exactly one food tile on the board
        self.assertEqual(1, sum([b.get_tile(Point(x, y)) == Tile.FOOD for x in range(7) for y in range(9)]))

    def test_get_set_tile(self):
        b = Board(7, 9, 3)
        b.set_tile(Point(2, 4), Tile.FOOD)
        self.assertEqual(b.get_tile(Point(2, 4)), Tile.FOOD)
        b.set_tile(Point(2, 4), Tile.EMPTY)
        self.assertEqual(b.get_tile(Point(2, 4)), Tile.EMPTY)
        b.set_tile(Point(2, 4), Tile.FOOD)
        self.assertEqual(b.get_tile(Point(2, 4)), Tile.FOOD)

    def test_snake_movement(self):
        b = Board(7, 9, 3)

        # Manually setting food pos
        b.set_food_pos(Point(6, 5))
        logger.info(f'Test board:\n{b}')

        # Moving the snake forward twice until it is at the wall
        e = b.move_snake(RelativeDirection.AHEAD)  # Head: (5, 4)
        self.assertTrue(e.alive)
        self.assertFalse(e.ate_food)
        e = b.move_snake(AbsoluteDirection.RIGHT)  # Head: (6, 4)
        self.assertTrue(e.alive)
        self.assertFalse(e.ate_food)

        # Moving snake down
        e = b.move_snake(RelativeDirection.RIGHT)  # Head: (6, 5)
        self.assertTrue(e.alive)
        self.assertTrue(e.ate_food)

        e = b.move_snake(AbsoluteDirection.DOWN)   # Head: (6, 6)
        self.assertFalse(e.ate_food)
        self.assertTrue(e.alive)

        # Spawn new food
        b.set_food_pos(Point(6, 7))

        # Moving further down
        e = b.move_snake(AbsoluteDirection.DOWN)   # Head: (6, 7)
        self.assertTrue(e.ate_food)
        self.assertTrue(e.alive)

        # Crashing into itself
        b.move_snake(AbsoluteDirection.LEFT)
        b.move_snake(AbsoluteDirection.UP)
        e = b.move_snake(AbsoluteDirection.RIGHT)
        self.assertFalse(e.alive)
        self.assertFalse(e.ate_food)

    # noinspection DuplicatedCode
    def test_wall_crashing_up(self):
        b = Board(7, 9, 3)
        events = [b.move_snake(AbsoluteDirection.UP) for _ in range(4)]
        self.assertTrue(all([event for event in events]))
        e = b.move_snake(AbsoluteDirection.UP)
        self.assertFalse(e.alive)

    def test_wall_crashing_left(self):
        b = Board(7, 9, 3)
        b.move_snake(AbsoluteDirection.UP)  # Turning around
        events = [b.move_snake(AbsoluteDirection.LEFT) for _ in range(4)]
        self.assertTrue(all([event for event in events]))
        e = b.move_snake(AbsoluteDirection.LEFT)
        self.assertFalse(e.alive)

    # noinspection DuplicatedCode
    def test_wall_crashing_down(self):
        b = Board(7, 9, 3)
        events = [b.move_snake(AbsoluteDirection.DOWN) for _ in range(4)]
        self.assertTrue(all([event for event in events]))
        e = b.move_snake(AbsoluteDirection.DOWN)
        self.assertFalse(e.alive)

    def test_wall_crashing_right(self):
        # Crashing into walls
        b = Board(7, 9, 3)
        events = [b.move_snake(AbsoluteDirection.RIGHT) for _ in range(2)]
        self.assertTrue(all([event for event in events]))
        e = b.move_snake(AbsoluteDirection.RIGHT)
        self.assertFalse(e.alive)

    def test_is_in_bounds(self):
        b = Board(7, 9, 3)
        for x in range(7):
            for y in range(9):
                self.assertTrue(b.is_in_bounds(Point(x, y)))
        self.assertFalse(b.is_in_bounds(Point(-1, 2)))
        self.assertFalse(b.is_in_bounds(Point(-1, -1)))
        self.assertFalse(b.is_in_bounds(Point(2, -1)))
        self.assertFalse(b.is_in_bounds(Point(0, 10)))
        self.assertFalse(b.is_in_bounds(Point(8, 0)))
        self.assertFalse(b.is_in_bounds(Point(10, 10)))
