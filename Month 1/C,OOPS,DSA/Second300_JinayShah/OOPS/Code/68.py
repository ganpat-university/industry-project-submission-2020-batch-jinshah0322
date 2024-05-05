class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def display(self):
        for row in self.grid:
            print("|".join(str(piece) if piece else " " for piece in row))
            print("-" * 17)

    def place_piece(self, piece, row, col):
        self.grid[row][col] = piece


class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        raise NotImplementedError("Subclasses must implement this method")


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = "♙" if color == "white" else "♟"

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        direction = 1 if self.color == "white" else -1
        if start_col == end_col and start_row + direction == end_row and board[end_row][end_col] is None:
            return True
        return False


class Player:
    def __init__(self, color):
        self.color = color


class Game:
    def __init__(self):
        self.board = Board()
        self.players = {"white": Player("white"), "black": Player("black")}

    def initialize_pieces(self):
        for color in ["white", "black"]:
            row = 0 if color == "black" else 7
            for col in range(8):
                pawn = Pawn(color)
                self.board.place_piece(pawn, row, col)

    def play(self):
        self.initialize_pieces()
        self.board.display()



chess_game = Game()
chess_game.play()