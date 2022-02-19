import random
import time

# Charlie King

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
        while True:
            try:
                row = int(input("Enter a row: "))
                col = int(input("Enter a col: "))
            except ValueError:
                print("Please enter a valid move.")
            else:
                if self.is_valid_move(int(row), int(col)):
                    break
                else:
                    print("Please enter a valid move.")
        self.place_player(player, int (row), int (col))
        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        if player == "X":
            self.take_manual_turn(player)
        if player == "O":
            self.take_minimax_turn(player, 100)
        return

    def take_random_turn(self, player):
        # TODO: randomly place a piece on an available space on the board
        row = random.randint(0,2)
        col = random.randint(0,2)
        while self.is_valid_move(row, col) is False:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        self.board[row][col] = player
        return

    def minimax(self, player, depth):
        # base case
        if self.check_win("X"):
            return -10, None, None
        elif self.check_win("O"):
            return 10, None, None
        elif self.check_tie():
            return 0, None, None
        if depth == 0:
            return 0, None, None

            # recursive case
        opt_row = -1
        opt_col = -1
        if player == "O":
            best = -100
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("O", row, col)
                        new_depth = depth - 1
                        score = self.minimax("X", new_depth)[0]
                        self.place_player("-", row, col)
                        if best < score:
                            best = score
                            opt_row = row
                            opt_col = col
            return best, opt_row, opt_col
        if player == "X":
            worst = 100
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("X", row, col)
                        new_depth = depth - 1
                        score = self.minimax("O", new_depth)[0]
                        self.place_player("-", row, col)
                        if worst > score:
                            worst = score
                            opt_row = row
                            opt_col = col
            return worst, opt_row, opt_col

    def minimax_alpha_beta(self, player, depth, alpha, beta):
        # base case
        if self.check_win("X"):
            return -10, None, None
        elif self.check_win("O"):
            return 10, None, None
        elif self.check_tie():
            return 0, None, None
        if depth == 0:
            return 0, None, None

            # recursive case
        opt_row = -1
        opt_col = -1
        if player == "O":
            best = -100
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("O", row, col)
                        new_depth = depth - 1
                        score = self.minimax_alpha_beta("X", new_depth, alpha, beta)[0]
                        self.place_player("-", row, col)
                        if best < score:
                            best = score
                            opt_row = row
                            opt_col = col
                            alpha = score
                        if alpha >= beta:
                            break
            return best, opt_row, opt_col
        if player == "X":
            worst = 100
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        self.place_player("X", row, col)
                        new_depth = depth - 1
                        score = self.minimax_alpha_beta("O", new_depth, alpha, beta)[0]
                        self.place_player("-", row, col)
                        if worst > score:
                            worst = score
                            opt_row = row
                            opt_col = col
                            beta = score
                        if alpha >= beta:
                            break
            return worst, opt_row, opt_col

    def take_minimax_turn(self, player, depth):
        start = time.time()
        # score, row, col = self.minimax(player, depth)
        score, row, col = self.minimax_alpha_beta(player, depth, -1000, 1000)
        end = time.time()
        self.place_player(player, row, col)
        print("This turn took:", end - start, "seconds")

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

