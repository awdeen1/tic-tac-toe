class User:
    def __init__(self, name, appearance):
        # User class stores all the moves and other data important to the game
        self.moves = []
        self.appearance = appearance
        self.name = name


class TicTacToe:
    def __init__(self):
        # Calls two instances of the user class with their respective name and appearance
        self.user_1 = User(name="User 1", appearance="X")
        self.user_2 = User(name="User 2", appearance="O")

        # Keeps track of the current user and if somebody has won yet
        self.winner = False
        self.current_user = self.user_1

        # The board uses a dictionary with the values being the visual appearance of each square
        self.board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

    def check_winner(self, user):
        # Set of combinations that trigger a win
        winning_combinations = [
            {"1", "2", "3"},
            {"4", "5", "6"},
            {"7", "8", "9"},
            {"1", "4", "7"},
            {"2", "5", "8"},
            {"3", "6", "9"},
            {"1", "5", "9"},
            {"3", "5", "7"}
        ]

        # Takes a respective user's moves and turns it into a set
        user_set = set(user.moves)

        # Checks if a winning set is a subset of the user set which checks if the user won
        for combo in winning_combinations:
            if combo.issubset(user_set):
                print(f"{user.name} is the winner!")
                self.winner = True
                self.print_board()

        # Takes care of draws
        if len(user.moves) == 5:
            print(f"It's a draw!")
            self.winner = True
            self.print_board()

    def play_move(self, move, user):
        # Checks if the value spot of the board has an X or and O, indicating an already played move
        if self.board[move] != " ":
            return print("Move already played!")

        # Changes the value of the board to reflect the user's move visually and logically
        self.board[move] = user.appearance
        user.moves.append(move)

        self.check_winner(user)

        # Changes current user each turn assuming the move was valid
        if self.current_user == self.user_1:
            self.current_user = self.user_2

        elif self.current_user == self.user_2:
            self.current_user = self.user_1

    def print_board(self):
        print(f"1 {self.board["1"]} | 2 {self.board["2"]} | 3 {self.board["3"]}\n"
                f"-----------\n"
                f"4 {self.board["4"]} | 5 {self.board["5"]} | 6 {self.board["6"]}\n"
                f"-----------\n"
                f"7 {self.board["7"]} | 8 {self.board["8"]} | 9 {self.board["9"]}")

