"""
SmartSnakes - by Buckfae
"""

from smart_snakes.game.board import Board

def main():
    """Plays snake using the magical power of AI"""

    print(f'Smart Snakes - by Buckfae')

    sample_board = Board(5, 5, 2)

    print(f'Board size: {sample_board.get_size()}')

    print(sample_board)

if __name__ == '__main__':
    main()
