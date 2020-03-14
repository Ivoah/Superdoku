def backtrack(board, d=0):
    if board and board.solved(): return board

    moves = sorted([(pos, board.validMoves(*pos)) for pos in board.emptyCells()], key=lambda m: len(m[1]))
    moves = expand(moves)
    # print(d, len(moves))

    for (row, col), move in moves:
        # print(f'{" "*d}({row}, {col}): {move}')
        newBoard = board.copy()
        newBoard.makeMove(row, col, move)
        newBoard = ac3(newBoard)
        if newBoard is None: continue
        newBoard = backtrack(newBoard, d + 1)
        if newBoard and newBoard.solved(): return newBoard

    return None

def expand(moves):
    return [(pos, move) for pos, vals in moves for move in vals]

def ac3(board):
    def revise(i, j):
        revised = False
        for a in domains[i]:
            newBoard = board.copy()
            newBoard.makeMove(*i, a)
            if all(b not in newBoard.validMoves(*j) for b in domains[j]):
                domains[i].remove(a)
                revised = True
        return revised

    queue = [(i, j) for i in board.emptyCells() for j in board.dependsOn(*i)]
    domains = {p: board.validMoves(*p) for p in board.emptyCells()}

    while queue:
        i, j = queue.pop(0)
        if revise(i, j):
            if len(domains[i]) == 0: return None
            for k in board.dependsOn(*i):
                queue.append((k, i))
    
    newBoard = board.copy()
    for p in domains:
        if len(domains[p]) == 1:
            newBoard.makeMove(*p, domains[p][0])
    return newBoard

if __name__ == '__main__':
    from Board import Board
    import sys

    with open(sys.argv[1]) as f:
        for puzzle in f.read().split():
            initial = Board(puzzle)
            solved = backtrack(initial)
            solved.printBoard()
