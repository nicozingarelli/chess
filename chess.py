import Pieces
from Pieces import Pawn
from Pieces import Knight
from Pieces import Bishop
from Pieces import Rook
from Pieces import Queen
from Pieces import King
from Board import Board
from timeit import default_timer as timer

def main():
    input = [['_', '_', '_', '_', 'k', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', 'p', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', 'B', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_']]
    # input = [['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', 'p', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', 'N', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_']]
    # input = [['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', 'p', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', 'N', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_']]
    # input = [['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', 'N', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_']]
    # input = [['_', '_', '_', '_', '_', '_', 'q', 'k'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', 'P', '_', 'p'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', '_', '_', '_'],
    #          ['_', '_', '_', '_', '_', 'P', 'Q', 'P'],
    #          ['_', '_', '_', '_', '_', 'P', 'P', '_'],
    #          ['_', '_', '_', '_', 'R', '_', 'K', '_']]
    # input = [['_', '_', 'B', '_', '_', '_', '_', '_'],
    #         ['_', '_', '_', '_', '_', '_', '_', '_'],
    #         ['_', '_', '_', 'K', '_', '_', '_', '_'],
    #         ['_', 'p', '_', '_', '_', '_', '_', '_'],
    #         ['_', '_', 'k', '_', '_', '_', '_', '_'],
    #         ['P', '_', '_', '_', '_', 'P', '_', '_'],
    #         ['_', 'B', '_', '_', '_', '_', '_', '_'],
    #         ['N', '_', '_', '_', '_', 'N', '_', '_']]

    board = Board(input)
    # print(len(board.getAllMoves('b')))
    board.updateBoard()
    for row in board.board:
        print(row)
    #
    # print(board.scoreBoard())
    # print(board.testMove([board.white_pieces[1], 0, 6]))
    # for row in board.board:
    #     print(row)
    # print(board.scoreBoard())
    # game = Game(board)
    # print(board.pickBestMove(Pieces.color.WHITE))
    # minimax(self, board, depth, player)
    start = timer()
    # print(board.minimax(board.board, 4, Pieces.color.BLACK))
    nextMove = board.minimax(board.board, 4, Pieces.color.WHITE)
    print("nextMove: ", nextMove[0])
    print("oi")
    print(nextMove[0][0] in board.black_pieces)
    board.makeMove(nextMove[0])
    board.updateBoard()
    print('')
    for row in board.board:
        print(row)
    end = timer()
    print(end - start)
    print(len(board.check_spots))
    print("isCheck? ", board.isCheck(Pieces.color.BLACK))

class Game(object):
    def __init__(self, board):
        self.board = board
        self.turn_count = 0

main()
