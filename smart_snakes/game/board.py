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

        move_dir: AbsoluteDirection
        if type(direction) == RelativeDirection:
            move_dir = self.target_dir.relative(direction)
        else:
            move_dir = direction

        logger.info(f'Moving snake: {move_dir}')
        next_tile = self.snake_coords[-1].get_point_in_direction(move_dir)
        logger.info(f'Next tile: {move_dir}')

        # Snake hit a wall
        if not self.is_in_bounds(next_tile):
            logger.info(f'Snake hit a wall: {next_tile}')
            return SnakeEvent(False, False)

        # Snake hit itself
        if self.get_tile(next_tile) == Tile.BODY:
            logger.info(f'Snake hit itself: {next_tile}')
            return SnakeEvent(False, False)

        # Snake ate food
        ate_food = self.get_tile(next_tile) == Tile.FOOD
        logger.info(f'Snake ate food: {ate_food}')

        # Setting old head as body tile
        self.set_tile(self.snake_coords[-1], Tile.BODY)

        # New head tile
        self.set_tile(next_tile, Tile.HEAD)
        self.snake_coords.append(next_tile)

        if not ate_food:
            self.set_tile(self.snake_coords[0], Tile.EMPTY)
            self.snake_coords = self.snake_coords[1:]
        else:
            self.spawn_new_food()

        self.target_dir = move_dir

        logger.info(f'New head: {self.snake_coords[-1]}')
        logger.info(f'Board:\n{self.__str__()}')

        return SnakeEvent(True, ate_food)

    def is_in_bounds(self, pos: Point) -> bool:
        size_x, size_y = self.get_size()
        return 0 <= pos.x < size_x and 0 <= pos.y < size_y

    def is_empty(self, pos: Point) -> bool:
        return self._board[pos.y][pos.x] == Tile.EMPTY.value

    def get_tile(self, pos: Point) -> Tile:
        return Tile(self._board[pos.y][pos.x])

    def set_tile(self, pos: Point, tile: Tile):
        """Sets tile at the given pos
        """
        self._board[pos.y][pos.x] = tile.value

    def set_food_pos(self, pos: Point):
        self._board[self._board == Tile.FOOD.value] = Tile.EMPTY.value
        self.set_tile(pos, Tile.FOOD)
        self.food_pos = pos

    def spawn_new_food(self) -> Point:
        while True:
            food_pos = Point(random.randint(0, self.get_size()[0] - 1), random.randint(0, self.get_size()[1] - 1))
            logger.info(f'Spawned food at {food_pos}')
            if self.is_empty(food_pos):
                break
        self.set_food_pos(food_pos)
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
