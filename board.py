import collections
from pieces import Pawn
from pieces import Knight
from pieces import Bishop
from pieces import Rook
from pieces import Queen
from pieces import King

B = -1
W = +1

class Board(object):
    def __init__(self, board):
        self.board = board
        self.pieces = self.generatePieces()
        self.white_pieces = self.pieces[0]
        self.black_pieces = self.pieces[1]


    def pickBestMove(self, side):
        if(side == 'w'):
            move_dict = { }
            for piece in self.white_pieces:
                potential_moves = piece.findMoves(self.board)
                for move in potential_moves:
                    score = self.testMove(move)
                    move_dict[score] = move
            od = collections.OrderedDict(sorted(move_dict.items(), reverse=True))
            return next(iter(od.items()))[1]
        if(side == 'b'):
            move_dict = { }
            for piece in self.black_pieces:
                potential_moves = piece.findMoves(self.board)
                for move in potential_moves:
                    score = self.testMove(move)
                    move_dict[score] = move
            od = collections.OrderedDict(sorted(move_dict.items()))
            return next(iter(od.items()))[1]


    def testMove(self, move):
        piece = move[0]
        i = piece.i
        j = piece.j
        test_i = move[1]
        test_j = move[2]
        piece_char = self.board[i][j]
        temp_char = self.board[test_i][test_j]
        # piece.i = test_i
        # piece.j = test_j
        self.board[i][j] = '_'
        self.board[test_i][test_j] = piece_char
        # self.updateBoard()
        test_pieces = self.generatePieces()
        self.board[i][j] = piece_char
        self.board[test_i][test_j] = temp_char
        return self.scoreTestBoard(test_pieces)


    def getAllMoves(self, side):
        moves = []
        if(side == 'w'):
            for piece in self.white_pieces:
                moves.extend(piece.findMoves(self.board))
        else:
            for piece in self.black_pieces:
                moves.extend(piece.findMoves(self.board))
        return moves

    def scoreBoard(self):
        score = 0
        for piece in self.white_pieces:
            score += piece.r_val
        for piece in self.black_pieces:
            score -= piece.r_val
        return score

    def scoreTestBoard(self, pieces):
        score = 0
        for piece in pieces[0]:
            score += piece.r_val
        for piece in pieces[1]:
            score -= piece.r_val
        return score

    def updateBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.board[i][j] = '_'
        for piece in self.white_pieces:
            self.board[piece.i][piece.j] = piece.letter.upper()
        for piece in self.black_pieces:
            self.board[piece.i][piece.j] = piece.letter

    def generatePieces(self):
        white_pieces = []
        black_pieces = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if(self.board[i][j] == 'P'):
                    new_pawn = Pawn('w', i, j)
                    white_pieces.append(new_pawn)
                if(self.board[i][j] == 'p'):
                    new_pawn = Pawn('b', i, j)
                    black_pieces.append(new_pawn)
                if(self.board[i][j] == 'N'):
                    new_knight = Knight('w', i, j)
                    white_pieces.append(new_knight)
                if(self.board[i][j] == 'n'):
                    new_knight = Knight('b', i, j)
                    black_pieces.append(new_knight)
                if(self.board[i][j] == 'B'):
                    new_bishop = Bishop('w', i, j)
                    white_pieces.append(new_bishop)
                if(self.board[i][j] == 'b'):
                    new_bishop = Bishop('b', i, j)
                    black_pieces.append(new_bishop)
                if(self.board[i][j] == 'R'):
                    new_rook = Rook('w', i, j)
                    white_pieces.append(new_rook)
                if(self.board[i][j] == 'r'):
                    new_rook = Rook('b', i, j)
                    black_pieces.append(new_rook)
                if(self.board[i][j] == 'Q'):
                    new_queen = Queen('w', i, j)
                    white_pieces.append(new_queen)
                if(self.board[i][j] == 'q'):
                    new_queen = Queen('b', i, j)
                    black_pieces.append(new_queen)
                if(self.board[i][j] == 'K'):
                    new_king = King('w', i, j)
                    white_pieces.append(new_king)
                if(self.board[i][j] == 'k'):
                    new_king = King('b', i, j)
                    black_pieces.append(new_king)
        return[white_pieces, black_pieces]
