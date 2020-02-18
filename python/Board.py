import random

GREEN = '\033[0;32m'
RESET = '\033[0m'

class Board:
    def __init__(self, filled):
        self.board = [[' ' for col in range(9)] for row in range(9)]
        self.start = random.sample([(row, col) for row in range(9) for col in range(9)], filled)
        for loc in self.start:
            self.board[loc[0]][loc[1]] = random.choice(self.validMoves(*loc))

    def getRow(self, row):
        return self.board[row]

    def getCol(self, col):
        return [row[col] for row in self.board]

    def getBox(self, row, col):
        row = row//3*3
        col = col//3*3
        return [self.board[r][c] for r in range(row, row+3) for c in range(col, col+3)]

    def validMoves(self, row, col):
        return list(
            {1, 2, 3, 4, 5, 6, 7, 8, 9}
            - set(self.getRow(row))
            - set(self.getCol(col))
            - set(self.getBox(row, col)))

    def printBoard(self):
        print('┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓')
        for row in range(9):
            print('┃' + '┃'.join(
                '│'.join(
                    f' {GREEN}{v}{RESET} ' if (row, i+j) in self.start else f' {v} '
                    for j, v in enumerate(self.board[row][i:i+3]))
                for i in range(0, 9, 3)) + '┃')
            if (row+1)%3 == 0:
                if row != 8:
                    print('┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫')
            else:
                print('┠───┼───┼───╂───┼───┼───╂───┼───┼───┨')
        print('┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛')

if __name__ == '__main__':
    b = Board(25)
    b.printBoard()
