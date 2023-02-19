from enum import Enum


class Tile(Enum):
    EMPTY = 0
    FOOD = -1
    HEAD = 1
    BODY = 2

    def to_symbol(self):
        match self.value:
            case 0: return ' '
            case -1: return 'f'
            case 1: return 'O'
            case 2: return 'o'

