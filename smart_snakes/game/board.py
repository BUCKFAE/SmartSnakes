"""
Game Board

Handles the snake and movement
"""

from __future__ import annotations

import random
from dataclasses import dataclass

import numpy as np

from smart_snakes.game.directions.absolute_direction import AbsoluteDirection
from smart_snakes.game.directions.relative_direction import RelativeDirection
from smart_snakes.game.point import Point
from smart_snakes.game.tile import Tile
from smart_snakes.log.snake_logger import logger


@dataclass
class SnakeEvent:
    """SnakeEvent keeps track of everything that happens within a turn"""
    alive: bool
    ate_food: bool


class Board:
    """Board for the game"""

    def __init__(self,
                 size_x: int,
                 size_y: int,
                 snake_length: int
                 ):
        """Creates a new board with a new snake"""
        assert size_x > 2 and size_y > 2

        random.seed(1)

        self._size_x: int = size_x
        self._size_y: int = size_y

        self._board = np.zeros((self._size_y, self._size_x))

        assert snake_length + 2 < size_x
        assert snake_length < size_y

        # Spawning snake in the center
        spawn_y = size_y // 2
        spawn_x = 2

        self.snake_coords: list[Point] = []

        for x in range(snake_length):
            tile_type = Tile.HEAD if x == snake_length - 1 else Tile.BODY
            self._board[spawn_y][spawn_x + x] = tile_type.value
            self.snake_coords.append(Point(spawn_x + x, spawn_y))

        # Spawning food at a random position
        self.food_pos: Point = self.spawn_new_food()

        # Snake starts looking to the right
        self.target_dir: AbsoluteDirection = AbsoluteDirection.RIGHT

    def move_snake(self, direction: AbsoluteDirection | RelativeDirection) -> SnakeEvent:
        """Moves the snake in the specified direction
        :returns: SnakeEvent storing everything notable that occurred
        """

        raise NotImplementedError

    def is_empty(self, pos: Point) -> bool:
        return self._board[pos.y][pos.x] == Tile.EMPTY.value

    def get_tile(self, pos: Point) -> Tile:
        return Tile(self._board[pos.y][pos.x])

    def clear_tile(self, pos: Point):
        """Removes the tile at the given point
        Fails if nothing was on this tile previously
        """
        assert not self.is_empty(pos), f'Can not clear empty tile'
        self._board[pos.y][pos.x] = Tile.EMPTY.value

    def set_tile(self, pos: Point, tile: Tile):
        """Sets tile at the given pos
        Fails if the tile was not empty
        """
        assert self.is_empty(pos)
        assert tile is not Tile.EMPTY, f'Can not set non-empty tile'
        self._board[pos.y][pos.x] = tile.value

    def spawn_new_food(self) -> Point:
        while True:
            food_pos = Point(random.randint(0, self.get_size()[0] - 1), random.randint(0, self.get_size()[1] - 1))
            logger.info(f'Spawned food at {food_pos}')
            if self.is_empty(food_pos):
                break
        self.set_tile(food_pos, Tile.FOOD)
        return food_pos

    def get_food_pos(self) -> Point:
        return self.food_pos

    def __str__(self) -> str:
        s = "+" + "-" * self._size_x + '+'
        for y in self._board:
            s += '\n|'
            for x in y:
                s += Tile(x).to_symbol()
            s += '|'
        s += '\n' + "+" + "-" * self._size_x + '+'
        return s

    def get_size(self) -> tuple[int, int]:
        return self._size_x, self._size_y
