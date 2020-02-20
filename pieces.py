class Piece(object):
    # board[i][j]
    def __init__(self, side, i, j):
        self.side = side
        self.i = i
        self.j = j

    def oppositeTeams(self, board, i2, j2):
        if(board[i2][j2] == '_'):
            return False
        if(board[self.i][self.j].islower() and board[i2][j2].islower()) or (board[self.i][self.j].isupper() and board[i2][j2].isupper()):
            return False
        else:
            return True

    def sameTeams(self, board, i2, j2):
        if(board[self.i][self.j].islower() and board[i2][j2].islower()) or (board[self.i][self.j].isupper() and board[i2][j2].isupper()):
            return True
        else:
            return False

    def isValidMove(self, board, i2, j2):
        if(board[i2][j2] == '_'):
            return True
        if(board[self.i][self.j].islower() and board[i2][j2].islower()) or (board[self.i][self.j].isupper() and board[i2][j2].isupper()):
            return False
        else:
            return True

    def sideMultiplier(self):
        if(self.side == 'w'):
            return 1
        else:
            return -1

class Pawn(Piece):
    def __init__(self, side, i, j):
        super().__init__(side, i, j)
        self.r_val = 1
        self.letter = 'p'

    def findMoves(self, board):
        moves = []
        if(self.side == 'w'):
            if(self.i - 1 >= 0) and (board[self.i - 1][self.j] == '_'):
                moves.append([self, self.i - 1, self.j])
            if(self.i - 1 >= 0) and (self.j - 1 >= 0) and (board[self.i - 1][self.j - 1] != '_'):
                if(super().oppositeTeams(board, self.i - 1, self.j - 1)):
                    moves.append([self, self.i - 1, self.j - 1])
            if(self.i - 1 >= 0) and (self.j + 1 < 8) and (board[self.i - 1][self.j + 1] != '_'):
                if(super().oppositeTeams(board, self.i - 1, self.j + 1)):
                    moves.append([self, self.i - 1, self.j + 1])
        else:
            if(self.i + 1 < 8) and (board[self.i + 1][self.j] == '_'):
                moves.append([self, self.i + 1, self.j])
            if(self.i + 1 < 8) and (self.j - 1 >= 0) and (board[self.i + 1][self.j - 1] != '_'):
                if(super().oppositeTeams(board, self.i + 1, self.j - 1)):
                    moves.append([self, self.i + 1, self.j - 1])
            if(self.i + 1 < 8) and (self.j + 1 < 8) and (board[self.i + 1][self.j + 1] != '_'):
                if(super().oppositeTeams(board, self.i + 1, self.j + 1)):
                    moves.append([self, self.i + 1, self.j + 1])
        return moves

class Knight(Piece):
    def __init__(self, side, i, j):
        super().__init__(side, i, j)
        self.r_val = 3
        self.letter = 'n'

    def findMoves(self, board):
        moves = []
        if(self.i - 1 >= 0) and (self.j - 2 >= 0) and (super().isValidMove(board, self.i - 1, self.j - 2)):
            moves.append([self, self.i - 1, self.j - 2])
        if(self.i - 2 >= 0) and (self.j - 1 >= 0) and (super().isValidMove(board, self.i - 2, self.j - 1)):
            moves.append([self, self.i - 2, self.j - 1])
        if(self.i - 1 >= 0) and (self.j + 2 < 8) and (super().isValidMove(board, self.i - 1, self.j + 2)):
            moves.append([self, self.i - 1, self.j + 2])
        if(self.i - 2 >= 0) and (self.j + 1 < 8) and (super().isValidMove(board, self.i - 2, self.j + 1)):
            moves.append([self, self.i - 2, self.j + 1])
        if(self.i + 1 < 8) and (self.j - 2 >= 0) and (super().isValidMove(board, self.i + 1, self.j - 2)):
            moves.append([self, self.i + 1, self.j - 2])
        if(self.i + 2 < 8) and (self.j - 1 >= 0) and (super().isValidMove(board, self.i + 2, self.j - 1)):
            moves.append([self, self.i + 2, self.j - 1])
        if(self.i + 1 < 8) and (self.j + 2 < 8) and (super().isValidMove(board, self.i + 1, self.j + 2)):
            moves.append([self, self.i + 1, self.j + 2])
        if(self.i + 2 < 8) and (self.j + 1 < 8) and (super().isValidMove(board, self.i + 2, self.j + 1)):
            moves.append([self, self.i + 2, self.j + 1])
        return moves

class Bishop(Piece):
    def __init__(self, side, i, j):
        super().__init__(side, i, j)
        self.r_val = 3
        self.letter = 'b'

    def findMoves(self, board):
        moves = []
        temp_i = self.i - 1
        temp_j = self.j - 1
        while(temp_i >= 0) and (temp_j >= 0):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i -= 1
            temp_j -= 1

        temp_i = self.i + 1
        temp_j = self.j + 1
        while(temp_i < 8) and (temp_j < 8):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i += 1
            temp_j += 1

        temp_i = self.i - 1
        temp_j = self.j + 1
        while(temp_i >= 0) and (temp_j < 8):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i -= 1
            temp_j += 1

        temp_i = self.i + 1
        temp_j = self.j - 1
        while(temp_i < 8) and (temp_j >= 0):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i += 1
            temp_j -= 1
        return moves

class Rook(Piece):
    def __init__(self, side, i, j):
        super().__init__(side, i, j)
        self.r_val = 5
        self.letter = 'r'

    def findMoves(self, board):
        moves = []
        temp_i = self.i + 1
        while(temp_i < 8):
            if(super().oppositeTeams(board, temp_i, self.j)):
                moves.append([self, temp_i, self.j])
                break
            elif(super().sameTeams(board, temp_i, self.j)):
                break
            elif(board[temp_i][self.j] == '_'):
                moves.append([self, temp_i, self.j])
            temp_i += 1

        temp_i = self.i - 1
        while(temp_i >= 0):
            if(super().oppositeTeams(board, temp_i, self.j)):
                moves.append([self, temp_i, self.j])
                break
            elif(super().sameTeams(board, temp_i, self.j)):
                break
            elif(board[temp_i][self.j] == '_'):
                moves.append([self, temp_i, self.j])
            temp_i -= 1

        temp_j = self.j + 1
        while(temp_j < 8):
            if(super().oppositeTeams(board, self.i, temp_j)):
                moves.append([self, self.i, temp_j])
                break
            elif(super().sameTeams(board, self.i, temp_j)):
                break
            elif(board[self.i][temp_j] == '_'):
                moves.append([self, self.i, temp_j])
            temp_j += 1

        temp_j = self.j - 1
        while(temp_j >= 0):
            if(super().oppositeTeams(board, self.i, temp_j)):
                moves.append([self, self.i, temp_j])
                break
            elif(super().sameTeams(board, self.i, temp_j)):
                break
            elif(board[self.i][temp_j] == '_'):
                moves.append([self, self.i, temp_j])
            temp_j -= 1
        return moves


class Queen(Piece):
    def __init__(self, side, i, j):
        super().__init__(side, i, j)
        self.r_val = 9
        self.letter = 'q'

    def findMoves(self, board):
        moves = []
        temp_i = self.i + 1
        while(temp_i < 8):
            if(super().oppositeTeams(board, temp_i, self.j)):
                moves.append([self, temp_i, self.j])
                break
            elif(super().sameTeams(board, temp_i, self.j)):
                break
            elif(board[temp_i][self.j] == '_'):
                moves.append([self, temp_i, self.j])
            temp_i += 1

        temp_i = self.i - 1
        while(temp_i >= 0):
            if(super().oppositeTeams(board, temp_i, self.j)):
                moves.append([self, temp_i, self.j])
                break
            elif(super().sameTeams(board, temp_i, self.j)):
                break
            elif(board[temp_i][self.j] == '_'):
                moves.append([self, temp_i, self.j])
            temp_i -= 1

        temp_j = self.j + 1
        while(temp_j < 8):
            if(super().oppositeTeams(board, self.i, temp_j)):
                moves.append([self, self.i, temp_j])
                break
            elif(super().sameTeams(board, self.i, temp_j)):
                break
            elif(board[self.i][temp_j] == '_'):
                moves.append([self, self.i, temp_j])
            temp_j += 1

        temp_j = self.j - 1
        while(temp_j >= 0):
            if(super().oppositeTeams(board, self.i, temp_j)):
                moves.append([self, self.i, temp_j])
                break
            elif(super().sameTeams(board, self.i, temp_j)):
                break
            elif(board[self.i][temp_j] == '_'):
                moves.append([self, self.i, temp_j])
            temp_j -= 1
        temp_i = self.i - 1
        temp_j = self.j - 1
        while(temp_i >= 0) and (temp_j >= 0):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i -= 1
            temp_j -= 1

        temp_i = self.i + 1
        temp_j = self.j + 1
        while(temp_i < 8) and (temp_j < 8):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i += 1
            temp_j += 1

        temp_i = self.i - 1
        temp_j = self.j + 1
        while(temp_i >= 0) and (temp_j < 8):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i -= 1
            temp_j += 1

        temp_i = self.i + 1
        temp_j = self.j - 1
        while(temp_i < 8) and (temp_j >= 0):
            if(super().oppositeTeams(board, temp_i, temp_j)):
                moves.append([self, temp_i, temp_j])
                break
            elif(super().sameTeams(board, temp_i, temp_j)):
                break
            elif(board[temp_i][temp_j] == '_'):
                moves.append([self, temp_i, temp_j])
            temp_i += 1
            temp_j -= 1
        return moves

class King(Piece):
    def __init__(self, side, i, j):
        super().__init__(side, i, j)
        self.r_val = 0
        self.letter = 'k'

    def findMoves(self, board):
        moves = []
        if(self.i - 1 >= 0) and (super().isValidMove(board, self.i - 1, self.j)):
            moves.append([self, self.i - 1, self.j])
        if(self.j - 1 >= 0) and (super().isValidMove(board, self.i, self.j - 1)):
            moves.append([self, self.i, self.j - 1])
        if(self.i + 1 < 8) and (super().isValidMove(board, self.i + 1, self.j)):
            moves.append([self, self.i + 1, self.j])
        if(self.j + 1 < 8) and (super().isValidMove(board, self.i, self.j + 1)):
            moves.append([self, self.i, self.j + 1])
        if(self.i - 1 >= 0) and (self.j - 1 >= 0) and (super().isValidMove(board, self.i - 1, self.j - 1)):
            moves.append([self, self.i - 1, self.j - 1])
        if(self.i - 1 >= 0) and (self.j + 1 < 8) and (super().isValidMove(board, self.i - 1, self.j + 1)):
            moves.append([self, self.i - 1, self.j + 1])
        if(self.i + 1 < 8) and (self.j - 1 >= 0) and (super().isValidMove(board, self.i + 1, self.j - 1)):
            moves.append([self, self.i + 1, self.j - 1])
        if(self.i + 1 < 8) and (self.j + 1 < 8) and (super().isValidMove(board, self.i + 1, self.j + 1)):
            moves.append([self, self.i + 1, self.j + 1])
        return moves
