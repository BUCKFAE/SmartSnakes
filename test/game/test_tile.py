import unittest

from smart_snakes.game.tile import Tile


class TestTile(unittest.TestCase):

    def test_to_symbol(self):
        self.assertEqual(Tile.EMPTY.to_symbol(), ' ')
        self.assertEqual(Tile.FOOD.to_symbol(), 'f')
        self.assertEqual(Tile.HEAD.to_symbol(), 'O')
        self.assertEqual(Tile.BODY.to_symbol(), 'o')

    def test_to_number(self):
        self.assertEqual(Tile.EMPTY.value, 0)
        self.assertEqual(Tile.FOOD.value, -1)
        self.assertEqual(Tile.HEAD.value, 1)
        self.assertEqual(Tile.BODY.value, 2)
