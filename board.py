import collections
import Pieces
import time
from Pieces import Pawn
from Pieces import Knight
from Pieces import Bishop
from Pieces import Rook
from Pieces import Queen
from Pieces import King

class Board(object):
    def __init__(self, board):
        self.board = board
        self.pieces = self.generatePieces()
        self.white_pieces = self.pieces[0]
        self.black_pieces = self.pieces[1]
        self.check_spots = []
        self.getAllMoves(Pieces.color.WHITE)

    def isCheck(self, side):
        pieces = []
        king = self.getKing(side)
        king_coords = [king.i, king.j]
        if king_coords in self.check_spots:
            return True
        else:
            return False

    def getKing(self, side):
        pieces = []
        if(side == Pieces.color.WHITE):
            pieces = self.white_pieces
        else:
            pieces = self.black_pieces
        for piece in pieces:
            if isinstance(piece, Pieces.King):
                return piece

    def makeMove(self, move):
        piece = move[0]
        new_i = move[1]
        new_j = move[2]
        i = piece.i
        j = piece.j
        self.board[i][j] = '_'
        if(piece.side == Pieces.color.WHITE):
            self.board[new_i][new_j] = piece.letter.upper()
        else:
            self.board[new_i][new_j] = piece.letter
        self.pieces = self.generatePieces()
        self.white_pieces = self.pieces[0]
        self.black_pieces = self.pieces[1]
        self.getAllMoves(piece.side)


    def minimax(self, board, depth, player):
        pieces = []
        # decide whether objective is high score or low score
        if player == Pieces.color.WHITE:
            best = [None, -99999]
            pieces = self.generateTestPieces(board)[0]
        else:
            best = [None, 99999]
            pieces = self.generateTestPieces(board)[1]

        # see if no more moves to analyze
        if depth == 0:
            test_pieces = self.generateTestPieces(board)
            score = self.scoreTestBoard(test_pieces)
            return [None, score]

        # explore all possible moves from here
        # print('num pieces: ', len(pieces))
        for piece in pieces:
            potential_moves = piece.findMoves(board)
            # print('num moves for piece: ', len(potential_moves))
            for move in potential_moves:
                # save state
                piece = move[0]
                i = piece.i
                j = piece.j
                test_i = move[1]
                test_j = move[2]
                piece_char = board[i][j]
                temp_char = board[test_i][test_j]
                # make changes to state
                board[i][j] = '_'
                board[test_i][test_j] = piece_char
                        # test_pieces = self.generateTestPieces(board)
                # score this new state
                score = self.minimax(board, depth - 1, Pieces.color(int(-player)))
                # undo state changes
                board[i][j] = piece_char
                board[test_i][test_j] = temp_char
                # give ourselves a way to seee which move got us this score
                score[0] = move

                # see if currently explored move is the best
                if player == Pieces.color.WHITE:
                    # print('whites move')
                    # print('score[1]', score[1])
                    # print('best[1]', best[1])
                    if score[1] > best[1]:
                        # new best (highest) score found
                        best = score
                else:
                    # print('blacks move')
                    # print('score[1]', score[1])
                    # print('best[1]', best[1])
                    if score[1] < best[1]:
                        # new best (lowest) score found
                        best = score
        return best

    def pickBestMove(self, side):
        if(side == Pieces.color.WHITE):
            move_dict = { }
            for piece in self.white_pieces:
                potential_moves = piece.findMoves(self.board)
                for move in potential_moves:
                    score = self.testMove(move)
                    move_dict[score] = move
            od = collections.OrderedDict(sorted(move_dict.items(), reverse=True))
            return next(iter(od.items()))[1]
        if(side == Pieces.color.BLACK):
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
        self.board[i][j] = '_'
        self.board[test_i][test_j] = piece_char
        test_pieces = self.generatePieces()
        self.board[i][j] = piece_char
        self.board[test_i][test_j] = temp_char
        return self.scoreTestBoard(test_pieces)


    def getAllMoves(self, side):
        moves = []
        self.check_spots = []
        if(side == Pieces.color.WHITE):
            for piece in self.white_pieces:
                print(piece)
                moves.extend(piece.findMoves(self.board))
            for move in moves:
                self.check_spots.append([move[1], move[2]])
        else:
            for piece in self.black_pieces:
                moves.extend(piece.findMoves(self.board))
            for move in moves:
                self.check_spots.append([move[1], move[2]])

        # for move in moves:
        #     self.check_spots.append([move[1], move[2]])
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
                    white_pieces.append(Pawn(Pieces.color.WHITE, i, j))
                if(self.board[i][j] == 'p'):
                    black_pieces.append(Pawn(Pieces.color.BLACK, i, j))
                if(self.board[i][j] == 'N'):
                    white_pieces.append(Knight(Pieces.color.WHITE, i, j))
                if(self.board[i][j] == 'n'):
                    black_pieces.append(Knight(Pieces.color.BLACK, i, j))
                if(self.board[i][j] == 'B'):
                    white_pieces.append(Bishop(Pieces.color.WHITE, i, j))
                if(self.board[i][j] == 'b'):
                    black_pieces.append(Bishop(Pieces.color.BLACK, i, j))
                if(self.board[i][j] == 'R'):
                    white_pieces.append(Rook(Pieces.color.WHITE, i, j))
                if(self.board[i][j] == 'r'):
                    black_pieces.append(Rook(Pieces.color.BLACK, i, j))
                if(self.board[i][j] == 'Q'):
                    white_pieces.append(Queen(Pieces.color.WHITE, i, j))
                if(self.board[i][j] == 'q'):
                    black_pieces.append(Queen(Pieces.color.BLACK, i, j))
                if(self.board[i][j] == 'K'):
                    white_pieces.append(King(Pieces.color.WHITE, i, j))
                if(self.board[i][j] == 'k'):
                    black_pieces.append(King(Pieces.color.BLACK, i, j))
        return[white_pieces, black_pieces]

    def generateTestPieces(self, board):
        white_pieces = []
        black_pieces = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == 'P'):
                    white_pieces.append(Pawn(Pieces.color.WHITE, i, j))
                if(board[i][j] == 'p'):
                    black_pieces.append(Pawn(Pieces.color.BLACK, i, j))
                if(board[i][j] == 'N'):
                    white_pieces.append(Knight(Pieces.color.WHITE, i, j))
                if(board[i][j] == 'n'):
                    black_pieces.append(Knight(Pieces.color.BLACK, i, j))
                if(board[i][j] == 'B'):
                    white_pieces.append(Bishop(Pieces.color.WHITE, i, j))
                if(board[i][j] == 'b'):
                    black_pieces.append(Bishop(Pieces.color.BLACK, i, j))
                if(board[i][j] == 'R'):
                    white_pieces.append(Rook(Pieces.color.WHITE, i, j))
                if(board[i][j] == 'r'):
                    black_pieces.append(Rook(Pieces.color.BLACK, i, j))
                if(board[i][j] == 'Q'):
                    white_pieces.append(Queen(Pieces.color.WHITE, i, j))
                if(board[i][j] == 'q'):
                    black_pieces.append(Queen(Pieces.color.BLACK, i, j))
                if(board[i][j] == 'K'):
                    white_pieces.append(King(Pieces.color.WHITE, i, j))
                if(board[i][j] == 'k'):
                    black_pieces.append(King(Pieces.color.BLACK, i, j))
        return[white_pieces, black_pieces]
