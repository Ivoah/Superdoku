import scala.util.Random;

class Board(val start: Seq[(Int, Int)]) {
    val GREEN = "\u001b[0;32m"
    val RESET = "\u001b[0m"

    val board = Array.ofDim[Int](9, 9)

    def getRow(row: Int): Seq[Int] = board(row).toSeq
    def getCol(col: Int): Seq[Int] = (for (row <- board) yield row(col)).toSeq
    def getBox(row: Int, col: Int): Seq[Int] = for (r <- row/3*3 until row/3*3+3; c <- col/3*3 until col/3*3+3) yield board(r)(c)

    def validMoves(row: Int, col: Int): Set[Int] = 
        Set(1, 2, 3, 4, 5, 6, 7, 8, 9)
            .diff(getRow(row).toSet)
            .diff(getCol(col).toSet)
            .diff(getBox(row, col).toSet)
    
    def printBoard() = {
        println("┏━━━┯━━━┯━━━┳━━━┯━━━┯━━━┳━━━┯━━━┯━━━┓")
        for (row <- 0 until 9) {
            println("┃" + (for (i <- 0 until 9 by 3)
                yield (for ((v, j) <- board(row).slice(i, i+3).zipWithIndex)
                    yield if (start contains (row, i+j)) s" $GREEN${if (v != 0) v else ' '}$RESET " else s" ${if (v != 0) v else ' '} "
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
        val start = Random.shuffle(for (row <- 0 until 9; col <- 0 until 9) yield (row, col)).take(filled)
        val board = new Board(start)
        for (loc <- start)
            board.board(loc._1)(loc._2) = Random.shuffle(board.validMoves(loc._1, loc._2)).head

        board
    }
}
