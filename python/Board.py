import random

GREEN = '\033[0;32m'
RESET = '\033[0m'

class Board:
    def __init__(self, boardString):
        self.size = int(len(boardString)**(1/4))
        self.board = [[int(boardString[r*self.size**2 + c]) for c in range(self.size**2)] for r in range(self.size**2)]
        self.start = [(r, c) for r in range(self.size**2) for c in range(self.size**2) if self.board[r][c] != 0]
    
    def copy(self):
        return Board(self.asString())

    def getRow(self, row):
        return self.board[row]

    def getCol(self, col):
        return [row[col] for row in self.board]

    def getBox(self, row, col):
        row = row//self.size*self.size
        col = col//self.size*self.size
        return [self.board[r][c] for r in range(row, row+self.size) for c in range(col, col+self.size)]

    def validMoves(self, row, col):
        return list(
            set(range(1, self.size**2 + 1))
            - set(self.getRow(row))
            - set(self.getCol(col))
            - set(self.getBox(row, col)))
    
    def makeMove(self, row, col, move):
        self.board[row][col] = move
    
    def emptyCells(self):
        return [(r, c) for r in range(self.size**2) for c in range(self.size**2) if self.board[r][c] == 0]
    
    def solved(self):
        return self.emptyCells() == 0

    def asString(self):
        return ''.join(''.join(map(str, row)) for row in self.board)

    def __repr__(self):
        return f'Board(\'{self.asString()}\')'

    def printBoard(self):
        print('┏' + '┳'.join(['┯'.join(['━━━']*self.size)]*self.size) + '┓')
        for row in range(self.size**2):
            print('┃' + '┃'.join(
                '│'.join(
                    (f' {GREEN}{v}{RESET} ' if (row, i+j) in self.start else f' {v} ') if v != 0 else '   '
                    for j, v in enumerate(self.board[row][i:i+self.size]))
                for i in range(0, self.size**2, self.size)) + '┃')
            if (row+1)%self.size == 0:
                if row != self.size**2 - 1:
                    print('┣' + '╋'.join(['┿'.join(['━━━']*self.size)]*self.size) + '┫')
            else:
                print('┠' + '╂'.join(['┼'.join(['───']*self.size)]*self.size) + '┨')
        print('┗' + '┻'.join(['┷'.join(['━━━']*self.size)]*self.size) + '┛')
