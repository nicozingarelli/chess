from pieces import Pawn
from pieces import Knight
from pieces import Bishop
from pieces import Rook
from pieces import Queen
from pieces import King
from board import Board

def main():
    input = [['_', '_', '_', '_', '_', '_', 'q', 'k'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', 'P', '_', 'p'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', 'Q', 'P'],
             ['_', '_', '_', '_', '_', 'P', 'P', '_'],
             ['_', '_', '_', '_', 'R', '_', 'K', '_']]

    board = Board(input)
    print(len(board.getAllMoves('b')))
    board.updateBoard()
    # print(board.scoreBoard())
    # game = Game(board)

class Game(object):
    def __init__(self, board):
        self.board = board
        self.turn_count = 0

main()
