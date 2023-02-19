import unittest

from smart_snakes.game.board import Board
from smart_snakes.game.point import Point
from smart_snakes.game.tile import Tile


class TestBoard(unittest.TestCase):

    def test_get_size(self):
        b1 = Board(7, 9, 2)
        self.assertEqual(b1.get_size(), (7, 9))

    def test_board_operations(self):
        b = Board(7, 9, 3)
        print(b)

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

        # Clearing / setting tiles
        b.clear_tile(Point(2, 4))
        self.assertEqual(b.get_tile(Point(2, 4)), Tile.EMPTY)
        b.set_tile(Point(2, 4), Tile.FOOD)
        self.assertEqual(b.get_tile(Point(2, 4)), Tile.FOOD)

        # Clearing empty tile
        with self.assertRaises(AssertionError):
            b.clear_tile(Point(0, 1))

        # Setting non-empty tile
        with self.assertRaises(AssertionError):
            b.set_tile(Point(3, 4), Tile.BODY)
        with self.assertRaises(AssertionError):
            b.set_tile(b.get_food_pos(), Tile.BODY)

        # Setting tile to empty
        with self.assertRaises(AssertionError):
            b.set_tile(Point(0, 1), Tile.EMPTY)


    def test_snake_movement(self):
        b = Board(7, 9, 3)
        print(b)

        # Moving the snake forward twice until it is at the wall



