import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        rows, cols = (3, 3)
        self.board = [["-"]*rows for _ in range(cols)]
        return

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your pieces - the first to 3 in a row wins!")
        return

    def print_board(self):
        # TODO: Print the board
        print("    0   1   2")
        for i in range(3):
            print(i, "  ", end='')
            for j in range(3):
                print(self.board[i][j], "  ", end='')
            print()
        return

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if row > 2 or row < 0:
            return False
        if col > 2 or col < 0:
            return False
        if self.board[row][col] == "-":
            return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = int(input("Enter a row: "))
        col = int(input("Enter a col: "))
        while self.is_valid_move(row, col) is False:
            print("Please enter a valid move.")
            row = int(input("Enter a row: "))
            col = int(input("Enter a col: "))
        self.place_player(player, row, col)
        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        self.take_manual_turn(player)
        return

    def check_col_win(self, player):
        # TODO: Check col win
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[j][i] == player:
                    count = count + 1
            if count == 3:
                return True
            count = 0
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == player:
                    count = count + 1
            if count == 3:
                return True
            count = 0
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_diag_win(player) is True or self.check_row_win(player) is True or self.check_col_win(player) is True:
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        if self.check_win("X") is True:
            return False
        if self.check_win("O") is True:
            return False
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    print("yee")
                    return False
        return True

    def play_game(self):
        # TODO: Play game
        self.print_instructions()
        player1turn = True
        while (self.check_win("X") is False) & (self.check_win("O") is False) & (self.check_tie() is False):
            self.print_board()
            if player1turn is True:
                self.take_turn("X")
                player1turn = False
            else:
                self.take_turn("O")
                player1turn = True
        self.print_board()
        if self.check_win("X") is True:
            print("X wins!")
        elif self.check_win("O") is True:
            print("O wins!")
        else:
            print("Tie!")
        return

