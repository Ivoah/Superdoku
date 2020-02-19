import scala.util.Random;

class Board(val board: Seq[Seq[Int]]) {
    val GREEN = "\u001b[0;32m"
    val RESET = "\u001b[0m"

    def getRow(row: Int) = board(row).toSeq
    def getCol(col: Int) = (for (row <- board) yield row(col)).toSeq
    def getBox(row: Int, col: Int) = for (r <- row/3*3 until row/3*3+3; c <- col/3*3 until col/3*3+3) yield board(r)(c)

    def validMoves(row: Int, col: Int): Set[Int] = Set(1, 2, 3, 4, 5, 6, 7, 8, 9)
        .diff(getRow(row).toSet)
        .diff(getCol(col).toSet)
        .diff(getBox(row, col).toSet)

    def makeMove(row: Int, col: Int, v: Int) = new Board(
        for (r <- 0 until 9) yield (for (c <- 0 until 9) yield (if (r == row && c == col) v else board(r)(c)))
    )

    def emptySpaces() = for (r <- 0 until 9; c <- 0 until 9 if board(r)(c) == 0) yield (r, c)

    def printBoard() = {
        println("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")
        for (row <- 0 until 9) {
            println("┃" + (for (i <- 0 until 9 by 3)
                yield (for (v <- board(row).slice(i, i+3))
                    yield s" ${if (v != 0) v else ' '} "
                ).mkString("|")
            ).mkString("┃") + "┃")
            if ((row+1)%3 == 0) {
                if (row != 8) {
                    println("┣━━━┿━━━┿━━━╋━━━┿━━━┿━━━╋━━━┿━━━┿━━━┫")
                }
            } else {
                println("┠───┼───┼───╂───┼───┼───╂───┼───┼───┨")
            }
        }
        println("┗━━━┷━━━┷━━━┻━━━┷━━━┷━━━┻━━━┷━━━┷━━━┛")
    }
}

object Board {
    def apply(filled: Int) = {
        def recurse(board: Board, remaining: Int): Board = {
            remaining match {
                case 0 => board
                case _ =>
                    val pos = Random.shuffle(board.emptySpaces()).head
                    val move = Random.shuffle(board.validMoves(pos._1, pos._2)).head
                    recurse(board.makeMove(pos._1, pos._2, move), remaining - 1)
            }
        }

        recurse(new Board(for (r <- 0 until 9) yield for (c <- 0 until 9) yield 0), filled)
    }
}
