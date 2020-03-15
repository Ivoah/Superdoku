from Board import *
from Superdoku import *

from timeit import timeit
import random

with open('../solved.txt') as f:
    for i, puzzle in enumerate(f.read().split()):
        with open(f'{i}.txt', 'w') as out:
            board = Board(puzzle)
            filled = [(r, c) for r in range(board.size**2) for c in range(board.size**2)]
            t = 0
            while t < 1:
                t = timeit('backtrack(board)', number=1, globals=globals())
                out.write(f'{board.size**2**2 - len(filled)}, {t}\n')
                p = filled.pop(random.randint(0, len(filled) - 1))
                board.makeMove(*p, 0)
