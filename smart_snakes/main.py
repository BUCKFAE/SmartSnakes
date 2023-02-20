"""
SmartSnakes - by Buckfae
"""

import pygame

from smart_snakes.game.board import Board
from smart_snakes.game.directions.absolute_direction import AbsoluteDirection
from smart_snakes.game.directions.relative_direction import RelativeDirection
from smart_snakes.log.snake_logger import logger


def main():
    """Plays snake using the magical power of AI"""
    logger.info('Smart Snakes - by Buckfae')

    screen = pygame.display.set_mode([700, 900])

    board = Board(7, 9, 3)

    clock = pygame.time.Clock()

    running = True
    while running:

        clock.tick(1)

        logger.info(f'New Frame')

        move_dir = RelativeDirection.AHEAD

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                logger.info(f'Exiting!')
                running = False

            # Snake Movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_dir = AbsoluteDirection.UP
                elif event.key == pygame.K_a:
                    move_dir = AbsoluteDirection.LEFT
                elif event.key == pygame.K_s:
                    move_dir = AbsoluteDirection.DOWN
                elif event.key == pygame.K_d:
                    move_dir = AbsoluteDirection.RIGHT

        logger.info(f'Move direction: {move_dir}')
        e = board.move_snake(move_dir)
        if not e.alive:
            running = False

    pygame.quit()


if __name__ == '__main__':
    main()
