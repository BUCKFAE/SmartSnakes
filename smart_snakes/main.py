"""
SmartSnakes - by Buckfae
"""

from smart_snakes.game.board import Board
from smart_snakes.log.snake_logger import logger


def main():
    """Plays snake using the magical power of AI"""
    logger.info('Smart Snakes - by Buckfae')

    sample_board = Board(5, 5, 2)

    logger.info(f'Board size: {sample_board.get_size()}')
    logger.info(f'Sample board:\n{sample_board}')

if __name__ == '__main__':
    main()
